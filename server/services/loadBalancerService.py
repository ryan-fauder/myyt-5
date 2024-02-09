from dao.datanodeDAO import DataNodeDAO
from dao.videoInfoDAO import VideoInfoDAO
from modules.monitorate import Monitorate
from session import create_session

class LoadBalancerService:
    replica_factor = 3

    def filter_online_datanodes(self, datanodes) -> list[str]:
        selected_datanodes = []
        try:
            monitorate = Monitorate()
            for datanode in datanodes:
                id, alias = datanode
                try:
                    if monitorate.check_online(id, alias):
                        selected_datanodes.append(alias)
                        if len(selected_datanodes) == self.replica_factor:
                            break
                except Exception as e:
                    raise Exception(f"Falha ao verificar a disponibilidade do DataNode {alias}: {e}")
        except Exception as e:
            raise e

        return selected_datanodes

    def select_datanodes(self, session = create_session()) -> list[str]:
        try:
            with DataNodeDAO(session) as datanode_dao:
                datanodes = datanode_dao.least_qtt_videos()
            
            if datanodes:
                return self.filter_online_datanodes(datanodes)
            
        except Exception as e:
            print(f"Erro ao selecionar datanodes: {e}")
            raise e
        return []

    def list_datanodes(self, id_video, session = create_session()) -> list[str]:
        try:
            with VideoInfoDAO(session) as video_info_dao:
                datanodes = video_info_dao.datanodes(id_video)
            
            if datanodes:
                return self.filter_online_datanodes(datanodes)
            
        except Exception as e:
            print(f"Erro ao listar datanodes para o vídeo {id_video}: {e}")
            raise e
        return []

    def find_datanode(self, id_video) -> str:
        datanodes = self.list_datanodes(id_video)
        if datanodes:
            return datanodes[0]
        return 

if(__name__ == "__main__"):
    loadBalancer = LoadBalancerService()
    print("LIST")
    print(loadBalancer.list_datanodes(1))
    print("SELECT")
    print(loadBalancer.select_datanodes())
    print("SELECT")
    print(loadBalancer.find_datanode(1))
    print("SELECT")
    print(loadBalancer.find_datanode(2))