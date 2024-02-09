import random
from sqlalchemy import func
from models import DataNode, datanode_videoinfo_association
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.models import VideoInfo 
from session import create_session

class DataNodeDAO:
    def __init__(self, session: Session):
        if session is None:
            self.sessao = create_session()
            self.own_session = True
        else:
            self.sessao = session
            self.own_session = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            if exc_type is not None:
                self.sessao.rollback()
            else:
                self.sessao.commit()
        except SQLAlchemyError as e:
            print(f"Erro ao realizar commit ou rollback: {e}")
        finally:
            self.sessao.close()

    def add(self, id = None, alias = None, commit=True):
        try:
            datanode = self.find(alias)
            if not datanode:
                datanode = DataNode(id=id, alias=alias)
                self.sessao.add(datanode)
                
                if commit:
                    self.sessao.commit()
            return datanode
        except SQLAlchemyError as e:
            if commit:
                self.sessao.rollback()
            raise e

    def delete(self, id, commit=True):
        try:
            datanode = self.sessao.query(DataNode).filter_by(id=id).first()
            if datanode:
                self.sessao.delete(datanode)
                if commit:
                    self.sessao.commit()
            return datanode
        except SQLAlchemyError as e:
            if commit:
                self.sessao.rollback()
            raise e

    def get(self, id):
        try:
            datanode = self.sessao.query(DataNode).filter_by(id=id).first()
            return datanode
        except SQLAlchemyError as e:
            raise e

    def next_id(self):
        try:
            datanode = DataNode(alias="DATANODE")
            self.sessao.add(datanode)
            self.sessao.flush()
            return datanode.id
        except SQLAlchemyError as e:
            self.sessao.rollback()
            raise e

    def list(self):
        try:
            return self.sessao.query(DataNode).all()
        except SQLAlchemyError as e:
            raise e

    def find(self, alias):
        try:
            datanode = self.sessao.query(DataNode).filter_by(alias=alias).first()
            return datanode
        except SQLAlchemyError as e:
            raise e
    def qtt_videos(self, id):
        try:
            videos_count = (
                self.sessao.query(func.count(VideoInfo.id))
                .join(datanode_videoinfo_association)
                .join(DataNode)
                .filter(DataNode.id == id)
                .scalar()
            )
            return videos_count
        except SQLAlchemyError as e:
            raise e
    def total_video_size(self, id):
        try:
            total_size = (
                self.sessao.query(func.sum(VideoInfo.size))
                .join(datanode_videoinfo_association)
                .join(DataNode)
                .filter(DataNode.id == id)
                .scalar()
            )
            return total_size
        except SQLAlchemyError as e:
                raise e
    def least_qtt_videos(self):
        try:
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
        except SQLAlchemyError as e:
            raise e
    def least_total_size(self):
        try:
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
        except SQLAlchemyError as e:
            raise e
