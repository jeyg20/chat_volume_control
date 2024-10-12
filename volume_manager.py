import re
import subprocess
import time
from datetime import datetime


def tail_file(files):
    files.seek(0, 2)
    while True:
        line = files.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def run_amixer(volume_operation):
    try:
        result = subprocess.run(
            ["amixer", "set", "Master", f"5%{volume_operation}"],
            check=True,
            capture_output=True,
            text=True,
        )
        print("Command output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")


def get_chat_data(file):
    print("scanning chat")
    with open(file, "r", encoding="utf-8") as f:
        log_lines = tail_file(f)
        up = r":(.*?)\!.*?@.*?\.tmi\.twitch\.tv PRIVMSG #(.*?) :(.*?)up"
        down = r":(.*?)\!.*?@.*?\.tmi\.twitch\.tv PRIVMSG #(.*?) :(.*?)down"

        for line in log_lines:
            if re.search(up, line):
                run_amixer("+")
            elif re.search(down, line):
                run_amixer("-")
