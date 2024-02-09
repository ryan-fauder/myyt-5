from dao.datanodeDAO import DataNodeDAO
from interfaces import VideoDTO
from dao.videoInfoDAO import VideoInfoDAO
from services.loadBalancerService import LoadBalancerService
from session import create_session
from modules.playkite import Playkite
import rpyc

class ReplicationService:
    loadBalancer = LoadBalancerService()

    @staticmethod
    def store(video: VideoDTO, session = create_session()):
        try:
            id = video['id']
            with DataNodeDAO(session) as datanode_dao, VideoInfoDAO(session) as video_info_dao:
                datanodes = ReplicationService.loadBalancer.select_datanodes(session)
                for datanode_alias in datanodes:
                    datanode = datanode_dao.find(datanode_alias)
                    if not datanode:
                        print(f"Não foi encontrado datanode com alias {datanode_alias}")
                        continue
                    playkite = Playkite(datanode_alias)
                    response = playkite.store_video(video)
                    if response:
                        video_info_dao.associateDatanode(id, datanode)
                        return response
        except Exception as e:
            print('Um erro na replicação ocorreu')
            raise e

    @staticmethod
    def delete(id: int, session = create_session()):
        try:
            with DataNodeDAO(session) as datanode_dao, VideoInfoDAO(session) as video_info_dao:
                datanodes = ReplicationService.loadBalancer.list_datanodes(id)
                for datanode_alias in datanodes:
                    datanode = datanode_dao.find(datanode_alias)
                    playkite = Playkite(datanode_alias)
                    response = playkite.delete_video(id)
                    if response:
                        video_info_dao.associateDatanode(id, datanode)
                return id
        except Exception as e:
            print('Um erro na replicação ocorreu')
            raise e

    @staticmethod
    def stream(id, session = create_session()):
        try:
            with VideoInfoDAO(session) as video_info_dao:
                datanode_alias = ReplicationService.loadBalancer.find_datanode(id)
                if datanode_alias:
                    playkite = Playkite(datanode_alias)
                    response = playkite.stream_video(id)
                    if response:
                        return response
        except Exception as e:
            print('Um erro na replicação ocorreu')
            raise e