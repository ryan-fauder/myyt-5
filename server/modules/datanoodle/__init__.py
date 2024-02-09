import time
import rpyc

from .datanoodle import AbstractDataNoodle
from .interfaces import InvalidServiceNameError

class Datanoodle:
    def __init__(self, service_name: str):
        try:
            if service_name.startswith('DATANOODLE_'):
                connection = rpyc.connect_by_service(service_name)
                connection._config['sync_request_timeout'] = None
                self.server: AbstractDataNoodle = connection.root
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

    def register_datanode(self, id: str = None, alias: str = None):
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

    def delete_datanode(self, id: str = None):
        try:
            response = self.server.delete(id)
            if not response: 
                print("Um servidor já foi registrado com esse endereço")
                return
            print("Servidor foi registrado com sucesso")
            return response
        except Exception as e:
            print(f"Erro ao registrar datanode: {e}")
            raise e
