import socket
import json
from urllib.parse import urlparse

from modules.communikate.communication import Communication

from ..message.src import Request, Response
class Fetch:
    def split_endpoint(endpoint: str):
        url_parts = urlparse(endpoint)
        host = url_parts.hostname
        port = url_parts.port
        path = url_parts.path
        if(host == None or port == None): 
            raise Exception('Endpoint inválido')
        return host, int(port), path
    
    def handle_request(endpoint: str, callback: callable):
        try:
            host, port, path = Fetch.split_endpoint(endpoint) 
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((host, port))
            response = callback(path, client)
            client.close()
            return response
        except ConnectionRefusedError as e:
            raise Exception('Não foi possível estabelecer conexão com o servidor')
        except Exception as e:
            raise e
    
    def post(endpoint: str, data: dict):
        def method_post(path, socket):
            request = Request(method="post", path=path, data=data)
            Communication.send(socket, request.__dict__())
            response: Response = Response.__from__(Communication.receive(socket))
            return response.data
        return Fetch.handle_request(endpoint, method_post)

    def put(endpoint: str, data: dict):
        def method_put(path, socket):
            request = Request(method="put", path=path, data=data)
            Communication.send(socket, request.__dict__())
            response: Response = Response.__from__(Communication.receive(socket))
            return response.data
        return Fetch.handle_request(endpoint, method_put)
    
    def get(endpoint: str):
        def method_get(path, socket):
            request = Request(method="get", path=path)
            Communication.send(socket, request.__dict__())
            response: Response = Response.__from__(Communication.receive(socket))
            return response.data
        return Fetch.handle_request(endpoint, method_get)

    
    def delete(endpoint: str, data: dict):
        def method_delete(path, socket):
            request = Request(method="delete", path=path, data=data)
            Communication.send(socket, request.__dict__())
            response: Response = Response.__from__(Communication.receive(socket))
            return response.data
        return Fetch.handle_request(endpoint, method_delete)



if __name__ == '__main__':
    print(Fetch.split_endpoint('http://localhost:3000'))