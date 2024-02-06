from controllers.monitorController import MonitorController
from rpyc.utils.server import ThreadedServer

import threading
from services.statusManager import reset_status

if __name__ == "__main__":
    reset_status_thread = threading.Thread(target=reset_status)
    reset_status_thread.start()
    datanode_server = ThreadedServer(MonitorController, auto_register=True, protocol_config={'allow_public_attrs': True})
    print(f"Servidor {MonitorController.ALIASES} iniciado\n")
    datanode_server.start()