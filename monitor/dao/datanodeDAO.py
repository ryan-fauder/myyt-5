import random
from models import DataNode
from sqlalchemy.orm import Session


class DataNodeDAO:
    def __init__(self, session: Session):
        self.sessao = session
    def add(self, alias):
        datanode = self.find(alias)
        if not datanode:
            datanode = DataNode(alias=alias)
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
    def next_id(self):
        datanode = DataNode(alias="DATANODE")
        self.sessao.add(datanode)
        self.sessao.flush()
        self.sessao.close()
        return datanode.id
    def list(self):
        return self.sessao.query(DataNode)
    def find(self, alias):
        datanode = self.sessao.query(DataNode).filter_by(alias=alias).first()
        if datanode:
            return datanode
    def check_online(self, id):
        datanode = self.get(id)
        if(datanode.status == 'Online'):
            pass
    def reset_status(self):
        try:
            self.sessao.query(DataNode).update({DataNode.status: 'Offline'})
            self.sessao.commit()
        except:
            self.sessao.rollback()
    def set_status(self, id, status):
        try:
            if(status in ['Online', 'Offline', 'Busy']):
                datanode = self.get(id)
                datanode.status = status
                self.sessao.commit()
                return datanode
        except:
            self.sessao.rollback()
    def get_status(self, id):
        datanode = self.get(id)
        if datanode:
            return datanode.status
if __name__ == "__main__":
    from session import session
    datanode_dao = DataNodeDAO(session)
    datanode_mock = {
        "alias": "localhost",
    }
    datanode_dao.add(datanode_mock['alias'])

    datanode_mock = {
        "alias": "localhost",
    }

    datanode2 = datanode_dao.add(datanode_mock['alias'])

    datanode = datanode_dao.get(datanode2.id)
    print(f"Datanode obtido por ID {datanode.id}: {datanode.alias}")

    datanode_removido = datanode_dao.delete(datanode.id)
    print(f"Vídeo removido por ID {datanode_removido}")

    datanodes = datanode_dao.list()
    print("Todos os datanodes no banco de dados:")
    for datanode in datanodes:
        print(f"{datanode.id} - {datanode.alias}")
        video_dao = VideoInfoDAO(session)
        if(random.random() > 0.5): 
            video_dao.associateDatanode(1, datanode)
        if(random.random() > 0.5):    
            video_dao.associateDatanode(2, datanode)
        if(random.random() > 0.5): 
            video_dao.associateDatanode(3, datanode)
        print(f"{datanode_dao.total_video_size(datanode.id)} - {datanode_dao.qtt_videos(datanode.id)} ")
    print("RESULTADOS")
    print(f"{[ (dn.__dict__, qtt) for dn, qtt in datanode_dao.least_qtt_videos(3)]};")
    print(f" {[ (dn.__dict__, qtt) for dn, qtt in datanode_dao.least_total_size(3)]}")
    session.close()