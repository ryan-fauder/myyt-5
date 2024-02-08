from dao.datanodeDAO import DataNodeDAO
from dao.videoInfoDAO import VideoInfoDAO
from modules.message.src import Request, Response
from modules.monitorate.src import Monitorate
from session import session

class LoadBalancerService:
    replica_factor = 3
    videoInfoDAO = VideoInfoDAO(session)
    datanodeDAO = DataNodeDAO(session)

    def check_datanodes(self, datanodes):
        selected_datanodes = []
        monitorate = Monitorate()
        for datanode in datanodes:
            id, alias = datanode
            if monitorate.check_online(id, alias):
                selected_datanodes.append(alias)
                if len(selected_datanodes) == self.replica_factor:
                    break
        return selected_datanodes

    def select_datanodes(self) -> list[tuple[str]]:
        datanodes = self.datanodeDAO.least_qtt_videos()
        if datanodes:
            return self.check_datanodes(datanodes)

    def list_datanodes(self, id_video):
        datanodes = self.videoInfoDAO.datanodes(id_video)
        if datanodes:
            return self.check_datanodes(datanodes)
        return []
    def find_datanode(self, id_video):
        datanodes = self.list_datanodes(id_video)
        if datanodes:
            return datanodes[0]
        return []
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