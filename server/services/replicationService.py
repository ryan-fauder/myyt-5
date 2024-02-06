from dao.datanodeDAO import DataNodeDAO
from interfaces.datanode import VideoDTO
from dao.videoInfoDAO import VideoInfoDAO
from services.loadBalancerService import LoadBalancerService
from session import session
import rpyc

class ReplicationService:
    videoInfoDAO = VideoInfoDAO(session)
    datanodeDAO = DataNodeDAO(session)
    loadBalancer = LoadBalancerService()
    def store(video: VideoDTO):
        try:
            id = video['id']
            datanodes = ReplicationService.loadBalancer.select_datanodes()
            for datanode in datanodes:
                alias = datanode
                datanode = ReplicationService.datanodeDAO.find(alias)
                if not datanode:
                    print(f"Não foi encontrado datanode com alias {alias}")
                if not alias:
                    print(f"Alias não encontrado {alias}")
                    continue
                datanode_server = rpyc.connect_by_service(alias).root
                if not datanode_server:
                    print(f"Não foi possível se conectar ao servidor com alias {alias} - ReplicationService.store")
                    continue
                response = datanode_server.store(video['id'], video['title'], video['description'], video['blob'], video['size'])
                if(response):
                    ReplicationService.videoInfoDAO.associateDatanode(id, datanode)
            return video
        except Exception as e:
            print('Um erro na replicação ocorreu')

    def delete(id):
        try:
            datanodes = ReplicationService.loadBalancer.list_datanodes(id)
            for datanode in datanodes:
                host, port = datanode
                connection = rpyc.connect(host, port)
                datanode_server = connection.root
                response = datanode_server.delete(id)
                if(response):
                    ReplicationService.videoInfoDAO.associateDatanode(id, datanode)
            return id
        except Exception as e:
            print('Um erro na replicação ocorreu')
    def stream(id):
        try:
            datanode = ReplicationService.loadBalancer.find_datanode(id)
            host, port = datanode
            connection = rpyc.connect(host, port)
            datanode_server = connection.root
            response = datanode_server.stream(id)
            if(response):
                return response
        except Exception as e:
            print('Um erro na replicação ocorreu')
