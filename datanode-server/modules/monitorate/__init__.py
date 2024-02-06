import rpyc
import time
from environment import INTERVAL_PING
class Monitorate:
    def __init__(self):
        try:
            connection = rpyc.connect_by_service('MONITOR_SERVER')
            self.monitor = connection.root
        except Exception as e:
            print(f"Falha ao tentar se conectar ao serviço {'MONITOR_SERVER'}")
            raise e
    def register_datanode(self):
        try:
            alias = self.monitor.offer()
            if not alias: 
                print("Não foram encontradas ofertadas de Alias para o serviço em DATANODE")
                return
            print("Servidor foi registrado com sucesso")
            id, alias = self.monitor.store(alias)
            return id, alias
        except:
            print("Um erro ocorreu em Monirate.register_datanode")
    def check_alias(self, id, alias):
        try:
            response = self.monitor.check_alias(id, alias)
            if not response:
                print(f"Um servidor com {alias} não foi encontrado")
                return False
            print(f"Servidor {alias} já está registrado")
            return response
        except:
            print("Um erro ocorreu")
    def keep_alive(self, id):
        while True:
            try:
                self.monitor.ping(id)
            except Exception as e:
                print(f"Erro ao enviar ping para o servidor: {e}")
                break
            time.sleep(INTERVAL_PING)