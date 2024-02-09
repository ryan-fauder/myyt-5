class Request:
    def __init__(self, method, path, data = {}):
        self.method = method
        self.path = path
        self.data = data

    def __dict__(self):
        return  {
            "type": "request",
            "method": self.method,
            "path": self.path,
            "data": self.data,
        }
    
    def __from__(message: dict):
        return Request(message['method'], message['path'], message['data'])
    
class Response:

    def __init__(self, status, data):
        self.status = status
        self.data = data
    
    def __dict__(self):
        return  {
            "type": "response",
            "status": self.status,
            "data": self.data,
        }

    def __from__(message: dict):
        return Response(message['status'], message['data'])