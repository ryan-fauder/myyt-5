import rpyc
import time

class Monitorate:
    def __init__(self, ping_frequency=1):
        try:
            connection = rpyc.connect_by_service('MONITOR_SERVER')
            self.monitor = connection.root
            self.ping_frequency = ping_frequency
        except ConnectionRefusedError as cre:
            print(f"Falha ao tentar se conectar ao serviço 'MONITOR_SERVER': {cre}")
            raise cre
        except Exception as e:
            print(f"Erro inesperado ao conectar ao serviço 'MONITOR_SERVER': {e}")
            raise e

    def register_datanode(self):
        try:
            alias = self.monitor.offer()
            if not alias:
                print("Não foram encontradas ofertas de Alias para o serviço em DATANODE")
                return None, None
            print("Servidor foi registrado com sucesso")
            id, alias = self.monitor.store(alias)
            return id, alias
        except Exception as e:
            print(f"Erro ao registrar datanode: {e}")
            raise e

    def check_alias(self, id, alias):
        try:
            response = self.monitor.check_alias(id, alias)
            if not response:
                print(f"Um servidor com {alias} não foi encontrado")
                return False
            print(f"Servidor {alias} já está registrado")
            return response
        except Exception as e:
            print(f"Um erro ocorreu - Monitorate.check_alias: {e}")
            raise e

    def check_online(self, id, alias):
        try:
            response = self.monitor.check_online(id, alias)
            if not response:
                print(f"Um servidor com {alias} não está online")
                return False
            print(f"Servidor {alias} está online")
            return response
        except Exception as e:
            print(f"Um erro ocorreu - Monitorate.check_online: {e}")
            raise e

    def keep_alive(self, id):
        while True:
            try:
                self.monitor.ping(id)
            except Exception as e:
                print(f"Erro ao enviar ping para o servidor: {e}")
                break
            time.sleep(self.ping_frequency)
