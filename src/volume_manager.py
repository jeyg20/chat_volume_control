import logging
import re
import subprocess
import time

logger = logging.getLogger("chat_volume_manager")


def tail_file(file):
    """Generator to tail a file, yielding new lines as they are added."""
    file.seek(0, 2)
    while True:
        line = file.readline()
        if line:
            yield line
        else:
            time.sleep(0.1)


def run_amixer(increment: str, duration: int):
    """Adjust the volume using amixer."""
    try:
        commands = [["amixer", "set", "Master", increment]]
        for command in commands:
            result = subprocess.run(
                command,
                check=True,
                capture_output=True,
                text=True,
            )
            logging.info("Command output: %s", result.stdout)
            time.sleep(duration)
    except subprocess.CalledProcessError as e:
        logging.error("Error occurred while running amixer: %s", e)


def get_chat_data(file):
    """Scan chat logs for specific patterns and trigger volume adjustments."""
    logging.info("Scanning chat")
    pattern = re.compile(
        r":(\w+)\!.*?@.*?\.tmi\.twitch\.tv PRIVMSG #(\w+) :(.*?)(HORN 1000000|GIGAFART 1000000|TUBERIA 3000000)"
    )

    try:
        with open(file, "r", encoding="utf-8") as f:
            log_lines = tail_file(f)
            for line in log_lines:
                match = pattern.search(line)
                if match:
                    message_type = match.group(
                        4
                    )  # The specific message (HORN, GIGAFART, TUBERIA)
                    logger.info(f"Match found for: {message_type} in {match.group(3)}")

                    # Run the amixer task regardless of which message was found
                    run_amixer("2%", 5)
                    run_amixer("10%", 5)
    except FileNotFoundError:
        logging.error("The file %s was not found.", file)
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)

    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    get_chat_data("chat.log")
