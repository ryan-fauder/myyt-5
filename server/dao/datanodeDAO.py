import random
from sqlalchemy import func
from models import DataNode, datanode_videoinfo_association
from sqlalchemy.orm import Session

from models.models import VideoInfo 

class DataNodeDAO:
    def __init__(self, session: Session):
        self.sessao = session
    def add(self, id=None, alias=None):
        datanode = DataNode(id=id, alias=alias)
        self.sessao.add(datanode)
        self.sessao.commit()
        return datanode
    def delete(self, id):
        datanode = self.sessao.query(DataNode).filter_by(id=id).first()
        if datanode:
            self.sessao.delete(datanode)
            self.sessao.commit()
            return datanode
    def get(self, id):
        datanode = self.sessao.query(DataNode).filter_by(id=id).first()
        if datanode:
            return datanode
    def list(self):
        return self.sessao.query(DataNode)
    def find(self, alias):
        datanode = self.sessao.query(DataNode).filter_by(alias=alias).first()
        if datanode:
            return datanode
    def set_status(self, id, status):
        if(status in ['Online', 'Offline', 'Busy']):
            datanode = self.get(id)
            datanode.status = status
            self.sessao.commit()
            return datanode
    def get_status(self, id):
        datanode = self.get(id)
        if datanode:
            return datanode.status
    def qtt_videos(self, id):
        videos_count = (
            self.sessao.query(func.count(VideoInfo.id))
            .join(datanode_videoinfo_association)
            .join(DataNode)
            .filter(DataNode.id == id)
            .scalar()
        )
        return videos_count
    def total_video_size(self, id):
        total_size = (
            self.sessao.query(func.sum(VideoInfo.size))
            .join(datanode_videoinfo_association)
            .join(DataNode)
            .filter(DataNode.id == id)
            .scalar()
        )
        return total_size
    def least_qtt_videos(self):
        query_result = (
            self.sessao.query(
                DataNode.id,
                DataNode.alias, 
                func.coalesce(func.count(VideoInfo.id), 0).label('num_videos')
            )
            .outerjoin(DataNode.videoinfos)
            .group_by(DataNode)
            .order_by('num_videos')
            .all()
        )
        if(query_result):
            return [(id, alias) for id, alias, qtt in query_result]
    def least_total_size(self):
        query_result = (
            self.sessao.query(
                DataNode.id,
                DataNode.alias, 
                func.coalesce(func.sum(VideoInfo.size), 0).label('total_size')
            )
            .outerjoin(DataNode.videoinfos)
            .group_by(DataNode)
            .order_by('total_size')
            .all()
        )
        if(query_result):
            return [(id, alias) for id, alias, qtt in query_result]
if __name__ == "__main__":
    from session import session
    from .videoInfoDAO import VideoInfoDAO
    datanode_dao = DataNodeDAO(session)
    datanode_mock = {
        "alias": "localhost",
    }
    datanode_dao.add(alias=datanode_mock['alias'])

    datanode_mock = {
        "alias": "localhost",
    }

    datanode2 = datanode_dao.add(alias=datanode_mock['alias'])

    datanode = datanode_dao.get(datanode2.id)
    print(f"Datanode obtido por ID {datanode.id}: {datanode.alias}")

    datanode_removido = datanode_dao.delete(datanode.id)
    print(f"Vídeo removido por ID {datanode_removido}")

    datanodes = datanode_dao.list()
    print("Todos os datanodes no banco de dados:")
    for datanode in datanodes:
        print(f"{datanode.id} - {datanode.alias}")
        video_dao = VideoInfoDAO(session)
        # video_dao.associateDatanode(1, datanode)
        # video_dao.associateDatanode(2, datanode)
        # video_dao.associateDatanode(3, datanode)
        print(f"{datanode_dao.total_video_size(datanode.id)} - {datanode_dao.qtt_videos(datanode.id)} ")
    print("RESULTADOS")
    print(f"{[ (id, alias) for id, alias in datanode_dao.least_qtt_videos(3)]};")
    print(f" {[ (id, alias) for id, alias in datanode_dao.least_total_size(3)]}")
    session.close()