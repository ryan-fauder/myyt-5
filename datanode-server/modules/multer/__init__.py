import os
from typing import Generator
import uuid

class Multer:
    def __init__(self, path=''):
        self.path = path

    @staticmethod
    def create_filename():
        random_name = str(uuid.uuid4())
        return f"{random_name}.mp4"

    def write_file(self, file_generator: Generator[bytes, None, None]):
        try:
            filename = self.create_filename()
            file_path = os.path.join(self.path, filename)
            with open(file_path, 'wb') as file:
                for chunk in file_generator:
                    file.write(chunk)
            return file_path
        except Exception as e:
            raise RuntimeError(f"Erro ao escrever o arquivo: {e}")

    def read_file(self, filename: str):
        try:
            file_path = os.path.join(self.path, filename)
            if os.path.exists(file_path):
                with open(file_path, 'rb') as file:
                    while True:
                        chunk = file.read(1024)
                        if not chunk:
                            break
                        yield chunk
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
