import rpyc
import time
from .monitor import AbstractMonitor

class Monitorate:
    monitor_alias = 'MONITOR_SERVER'
    def __init__(self, ping_frequency=1):
        try:
            connection = rpyc.connect_by_service(self.monitor_alias)
            self.monitor: AbstractMonitor = connection.root
            self.ping_frequency = ping_frequency
        except ConnectionRefusedError as cre:
            print(f"Erro ao conectar ao serviço '{self.monitor_alias}': Conexão recusada - {cre}")
            raise cre
        except Exception as e:
            print(f"Erro inesperado ao conectar ao serviço '{self.monitor_alias}': {e}")
            raise e

    def register_datanode(self):
        try:
            alias = self.monitor.offer()
            if not alias:
                print("Nenhuma oferta de Alias encontrada para o serviço em {self.monitor_alias}")
                return None, None
            print("Registro do servidor concluído com sucesso")
            id, alias = self.monitor.store(alias)
            return id, alias
        except Exception as e:
            print(f"Erro ao registrar datanode: {e}")
            raise e

    def check_alias(self, id, alias):
        try:
            response = self.monitor.check_alias(id, alias)
            if not response:
                print(f"Um servidor com Alias '{alias}' não foi encontrado")
                return False
            print(f"Servidor com Alias '{alias}' já está registrado")
            return response
        except Exception as e:
            print(f"Erro ao verificar Alias - Monitorate.check_alias: {e}")
            raise e

    def check_online(self, id, alias):
        try:
            response = self.monitor.check_online(id, alias)
            if not response:
                print(f"O servidor com Alias '{alias}' não está online")
                return False
            print(f"Servidor com Alias '{alias}' está online")
            return response
        except Exception as e:
            print(f"Erro ao verificar online - Monitorate.check_online: {e}")
            raise e

    def keep_alive(self, id):
        while True:
            try:
                self.monitor.ping(id)
            except Exception as e:
                print(f"Erro ao enviar ping para o servidor: {e}")
                break
            time.sleep(self.ping_frequency)
