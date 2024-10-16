import logging
import threading
from logging.handlers import RotatingFileHandler

import chat_logger
from volume_manager import get_chat_data

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s — %(message)s",
    datefmt="%Y-%m-%d_%H:%M:%S",
    handlers=[
        logging.StreamHandler(),
        RotatingFileHandler(
            "./chat.log", maxBytes=1024 * 1024, backupCount=1, encoding="utf-8"
        ),
    ],
)

logger = logging.getLogger("chat_volume_manager")


def run_chat_logger():
    chat_logger.main()


def run_volume_manager():
    log_file = "./chat.log"
    get_chat_data(log_file)


def main():
    logger.info("Starting application...")

    chat_logger_thread = threading.Thread(target=run_chat_logger)
    volume_manager_thread = threading.Thread(target=run_volume_manager)

    chat_logger_thread.start()
    volume_manager_thread.start()

    chat_logger_thread.join()
    volume_manager_thread.join()


if __name__ == "__main__":
    main()
