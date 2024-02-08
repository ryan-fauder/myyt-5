from controllers.statisticController import StatisticController
from rpyc.utils.server import ThreadedServer

if __name__ == "__main__":
    statistics_server = ThreadedServer(StatisticController, auto_register=True, protocol_config={'allow_public_attrs': True})
    print(f"Servidor {StatisticController.ALIASES} iniciado\n")
    statistics_server.start()