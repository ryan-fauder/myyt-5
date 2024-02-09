from typing import Generator
import rpyc

from .playkite import AbstractPlaykite
from .interfaces import VideoDTO, InvalidServiceNameError

class Playkite:
    def __init__(self, service_name: str):
        try:
            if service_name.startswith('PLAYKITE_'):
                connection = rpyc.connect_by_service(service_name)
                connection._config['sync_request_timeout'] = None
                self.server: AbstractPlaykite = connection.root
            else:
                raise InvalidServiceNameError(f"O nome do serviço {service_name} não é válido.")
        except ConnectionRefusedError as cre:
            print(f"Falha ao tentar se conectar ao servidor {service_name}: {cre}")
            raise cre
        except InvalidServiceNameError as ise:
            print(ise)
            raise ise
        except Exception as e:
            print(f"Erro inesperado ao conectar ao servidor {service_name}: {e}")
            raise e

    def store_video(self, body: VideoDTO) -> VideoDTO:
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

    def stream_video(self, id: int) -> Generator[bytes, None, None]:
        try:
            response = self.server.stream(id)
            return response
        except Exception as e:
            print(f"Erro ao fazer streaming do vídeo: {e}")
            raise e