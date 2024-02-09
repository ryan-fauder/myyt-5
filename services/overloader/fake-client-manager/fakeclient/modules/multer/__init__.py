import os
from typing import Generator
import uuid
from ..statistikal import Statistikal
import time
class Multer:
    def __init__(self, path=''):
        self.path = path

    @staticmethod
    def create_filename():
        random_name = str(uuid.uuid4())
        return f"{random_name}.mp4"

    def write_file(self, file_generator: Generator[bytes, None, None], id_client):
        try:
            filename = self.create_filename()
            file_path = os.path.join(self.path, filename)
            statistikal = Statistikal()
            with open(file_path, 'wb') as file:
                
                for chunk in file_generator:
                    start_time = time.time()
                    file.write(chunk)
                    measured_time = time.time() - start_time
                    statistikal.register_statistic("chunk_write",  float(measured_time), str(id_client))
            return file_path            
            
        except Exception as e:
            raise RuntimeError(f"Erro ao escrever o arquivo: {e}")

    def read_file(self, filename: str, id_client):
        statistikal = Statistikal()
        def file_reader(file):
            while True:
                start_time = time.time()
                chunk = file.read(1024)
                measured_time = time.time() - start_time
                statistikal.register_statistic('chunk_write', float(measured_time), str(id_client))
                if not chunk:
                    break
                yield chunk
        try:
            file_path = os.path.join(self.path, filename)
            if os.path.exists(self.path):
                file = open(file_path, 'rb')
                return file_reader(file)
            else:
                raise FileNotFoundError(f"O arquivo '{filename}' não foi encontrado no diretório '{self.path}'.")
        except Exception as e:
            raise RuntimeError(f"Erro ao ler o arquivo: {e}")

    def remove_file(self, filename: str):
        try:
            file_path = os.path.join(self.path, filename)
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"Arquivo '{filename}' removido com sucesso.")
            else:
                raise FileNotFoundError(f"O arquivo '{filename}' não foi encontrado no diretório '{self.path}'.")
        except Exception as e:
            raise RuntimeError(f"Erro ao remover o arquivo: {e}")
