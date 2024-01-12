import socket
import os
from .router import Router
from .worker import Worker

class Dispatcher:
    router: Router = Router()
    def __init__(self, host, port):
        self.host = host
        self.port = int(port)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def listen(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

        while True:
            client, addr = self.server_socket.accept()
            worker = Worker(client, addr, self.router)
            worker.start()
    def Router(self):
        return self.router

if __name__ == "__main__":
    host = os.environ['server_host']
    port = os.environ['server_port']

    dispatcher = Dispatcher(host, port)
    dispatcher.listen()
