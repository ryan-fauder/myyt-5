from rpyc.utils.server import ThreadedServer

from controllers.videoController import VideoController
from modules.monitorate import Monitorate
from services.aliasManager import get_alias
import threading

if __name__ == "__main__":
    try:
        monitorate = Monitorate()
        id, alias = get_alias(monitorate)
        
        if alias:
            print(f"Alias {alias} recebido com sucesso")
            ping_thread = threading.Thread(target=monitorate.keep_alive, args=[id])
            ping_thread.start()
            
            VideoController.ALIASES = [alias]
            datanode_server = ThreadedServer(VideoController, auto_register=True, protocol_config={'allow_public_attrs': True})
            
            print(f"Servidor iniciado em {VideoController.ALIASES}")
            datanode_server.start()
    
    except Exception as e:
        print(f"Erro ao iniciar o servidor: {e}")