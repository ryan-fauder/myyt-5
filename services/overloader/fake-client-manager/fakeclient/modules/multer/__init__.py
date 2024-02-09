import os
from typing import Generator
import uuid
from ..statistikal import Statistikal
import time
class Multer:
    def __init__(self, path='', chunk_size=2**20):
        self.path = path
        self.chunk_size = chunk_size

    @staticmethod
    def create_filename():
        random_name = str(uuid.uuid4())
        return f"{random_name}.mp4"

    def write_file(self, file_generator: Generator[bytes, None, None], id_client):
        try:
            filename = self.create_filename()
            file_path = os.path.join(self.path, filename)
            statistikal = Statistikal()
            mean_time = 0
            total_chunks = 1
            with open(file_path, 'wb') as file:
                for chunk in file_generator:
                    start_time = time.time()
                    # Writing
                    file.write(chunk)
                    #
                    measured_time = time.time() - start_time
                    mean_time = (mean_time + measured_time) % 1000000007
                    total_chunks = (total_chunks + 1) % 1000000007
                mean_time /= total_chunks
                statistikal.register_statistic("chunk_write",  float(mean_time), str(id_client))
            return file_path            
            
        except Exception as e:
            raise RuntimeError(f"Erro ao escrever o arquivo: {e}")

    def read_file(self, filename: str, id_client):
        statistikal = Statistikal()

        def file_reader(file):
            mean_time = 0
            total_chunks = 1
            while True:
                start_time = time.time()
                # Reading
                chunk = file.read(self.chunk_size)
                #
                measured_time = time.time() - start_time
                mean_time = (mean_time + measured_time) % 1000000007
                total_chunks = (total_chunks + 1) % 1000000007
                if not chunk:
                    break
                yield chunk
            mean_time /= total_chunks
            statistikal.register_statistic("chunk_read",  float(mean_time), str(id_client))
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
