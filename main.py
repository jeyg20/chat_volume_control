import threading

import chat_logger
from volume_manager import get_chat_data


def run_chat_logger():
    chat_logger.main()


def run_volume_manager():
    log_file = "./chat.log"
    print("runnig")
    get_chat_data(log_file)


def main():
    chat_logger_thread = threading.Thread(target=run_chat_logger)
    volume_manager_thread = threading.Thread(target=run_volume_manager)

    chat_logger_thread.start()
    volume_manager_thread.start()

    chat_logger_thread.join()
    volume_manager_thread.join()


if __name__ == "__main__":
    main()
