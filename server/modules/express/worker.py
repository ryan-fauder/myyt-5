import threading
from ..communikate.communication import Communication
from ..message import Request, Response
from .router import Router
import socket
class Worker(threading.Thread):
    def __init__(self, client_socket: socket.socket, client_address, router: Router):
        super().__init__()
        self.client_socket = client_socket
        self.client_address = client_address
        self.router: Router = router
    def run(self):
        print(f"[*] Conexão aceita de {self.client_address[0]}:{self.client_address[1]}")
        message = Communication.receive(self.client_socket)
        request = Request.__from__(message)
        self.handle(request)

        self.client_socket.shutdown(socket.SHUT_RDWR)
        print(f"[*] Conexão encerrada com {self.client_address[0]}:{self.client_address[1]}")

    def handle(self, request: Request):
        try:
            callback_fn = self.router.callback(request.method, request.path)
            response: Response = callback_fn(request)
            return Communication.send(self.client_socket, response.__dict__())
        except Exception as e:
            Communication.send_error(self.client_socket, e)
