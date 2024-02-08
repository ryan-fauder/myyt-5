import time
import rpyc

from datanode import VideoDTO

class Replikate:
    def __init__(self, service_name):
        try:
            connection = rpyc.connect_by_service(service_name)
            self.server = connection.root
        except Exception as e:
            print(f"Falha ao tentar se conectar ao servidor Replikate {service_name}")
            raise e
    def register_datanode(self, id=None, alias=None):
        try:
            response = self.server.store(id, alias)
            if not response: 
                print("Um servidor já foi registrado com esse endereço")
                return
            print("Servidor foi registrado com sucesso")
            return response
        except:
            print("Um erro ocorreu")
    def keep_alive(self, id):
        while True:
            try:
                self.server.ping(id)
            except Exception as e:
                print(f"Erro ao enviar ping para o servidor: {e}")
            time.sleep(5)
    def store_video(self, body: VideoDTO):
        try:
            response = self.server.store(body)
            return response
        except:
            print("Um erro ocorreu")
    def index_videos(self):
        try:
            response = self.server.index()
            return response
        except:
            print("Um erro ocorreu")
    def delete_video(self, id: int):
        try:
            response = self.server.delete(id)
            return response
        except:
            print("Um erro ocorreu")
    def read_video(self, id: int):
        try:
            response = self.server.read(id)
            return response
        except:
            print("Um erro ocorreu")
    def stream_video(self, id: int):
        try:
            response = self.server.stream(id)
            return response
        except:
            print("Um erro ocorreu")