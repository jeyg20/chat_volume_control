import logging
import os
import socket

from dotenv import load_dotenv
from emoji import demojize

load_dotenv()

sock = socket.socket()

logger = logging.getLogger("chat_volume_manager")

server = "irc.chat.twitch.tv"
port = 6667
nickname = os.getenv("NICKNAME")
token = os.getenv("TOKEN")
channel = os.getenv("CHANNEL")


def main():
    logging.info("Chat logger has started.")
    sock = socket.socket()
    sock.connect((server, port))
    sock.send(f"PASS {token}\r\n".encode("utf-8"))
    sock.send(f"NICK {nickname}\r\n".encode("utf-8"))
    sock.send(f"JOIN {channel}\r\n".encode("utf-8"))

    try:
        while True:
            resp = sock.recv(2048).decode("utf-8")

            if resp.startswith("PING"):
                sock.send("PONG\n".encode("utf-8"))
            elif len(resp) > 0:
                logging.info(demojize(resp))

    except KeyboardInterrupt:
        logging.info("chat logger stopped.")
        sock.close()
        exit()


if __name__ == "__main__":
    main()
