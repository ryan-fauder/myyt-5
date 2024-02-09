import time
import rpyc

class Statistikal:
    def __init__(self):
        try:
            connection = rpyc.connect_by_service("STATISTIC_SERVER")
            self.server = connection.root
        except Exception as e:
            print(f"Falha ao tentar se conectar ao servidor Statistical {'STATISTIC_SERVER'}")
            raise e
    def register_statistic(self, topic, value, author):
        try:
            result = self.server.register(topic, value, author)
            print(result)
            return result
        except Exception as e:
            print(f"Erro ao registrar estatística: {str(e)}")
            raise e
    def retrieve_statistics(self):
        try:
            statistics = self.server.retrieve()
            return statistics
        except Exception as e:
            print(f"Erro ao recuperar estatísticas: {str(e)}")
            raise e
    def reset_statistics(self):
        try:
            statistics = self.server.reset()
            return statistics
        except Exception as e:
            print(f"Erro ao resetar estatísticas: {str(e)}")
            raise e