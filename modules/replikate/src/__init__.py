import time
import rpyc

from datanode import VideoDTO

class Replikate:
    def __init__(self, service_name):
        try:
            connection = rpyc.connect_by_service(service_name)
            connection._config['sync_request_timeout'] = None
            self.server = connection.root
        except ConnectionRefusedError as cre:
            print(f"Falha ao tentar se conectar ao servidor Replikate {service_name}: {cre}")
            raise cre
        except Exception as e:
            print(f"Erro inesperado ao conectar ao servidor Replikate {service_name}: {e}")
            raise e

    def register_datanode(self, id=None, alias=None):
        try:
            response = self.server.store(id, alias)
            if not response: 
                print("Um servidor já foi registrado com esse endereço")
                return
            print("Servidor foi registrado com sucesso")
            return response
        except Exception as e:
            print(f"Erro ao registrar datanode: {e}")
            raise e

    def keep_alive(self, id):
        while True:
            try:
                self.server.ping(id)
            except Exception as e:
                print(f"Erro ao enviar ping para o servidor: {e}")
                raise e
            time.sleep(5)

    def store_video(self, body: VideoDTO):
        try:
            response = self.server.store(body)
            return response
        except Exception as e:
            print(f"Erro ao armazenar vídeo: {e}")
            raise e

    def index_videos(self):
        try:
            response = self.server.index()
            return response
        except Exception as e:
            print(f"Erro ao indexar vídeos: {e}")
            raise e

    def delete_video(self, id: int):
        try:
            response = self.server.delete(id)
            return response
        except Exception as e:
            print(f"Erro ao deletar vídeo: {e}")
            raise e

    def read_video(self, id: int):
        try:
            response = self.server.read(id)
            return response
        except Exception as e:
            print(f"Erro ao ler vídeo: {e}")
            raise e

    def stream_video(self, id: int):
        try:
            response = self.server.stream(id)
            return response
        except Exception as e:
            print(f"Erro ao fazer streaming do vídeo: {e}")
            raise e