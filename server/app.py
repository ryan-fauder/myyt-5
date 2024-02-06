from controllers.replicationController import ReplicationController
from controllers.datanodeController import DataNodeController
from rpyc.utils.server import ThreadedServer
from threading import Thread

from environment import REPLIKATE_DATANODE_MANAGER_ALIASES, REPLIKATE_VIDEO_MANAGER_ALIASES

def start_datanode_manager():
    DataNodeController.ALIASES = [REPLIKATE_DATANODE_MANAGER_ALIASES]
    datanode_server = ThreadedServer(DataNodeController, auto_register=True, protocol_config={'allow_public_attrs': True})
    print(f"Servidor {DataNodeController.ALIASES} iniciado\n")
    datanode_server.start()

def start_video_manager():
    ReplicationController.ALIASES = [REPLIKATE_VIDEO_MANAGER_ALIASES]
    video_manager = ThreadedServer(ReplicationController, auto_register=True, protocol_config={'allow_public_attrs': True})
    print(f"Servidor {ReplicationController.ALIASES} iniciado\n")
    video_manager.start()

if __name__ == "__main__":
    datanode_thread = Thread(target=start_datanode_manager)
    video_thread = Thread(target=start_video_manager)

    datanode_thread.start()
    video_thread.start()

    datanode_thread.join()
    video_thread.join()
