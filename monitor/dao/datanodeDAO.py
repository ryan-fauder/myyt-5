from models import DataNode
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
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

    def add(self, alias, commit=True):
        try:
            datanode = self.find(alias)
            if not datanode:
                datanode = DataNode(alias=alias)
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
            datanode = DataNode(alias="DT")
            self.sessao.add(datanode)
            self.sessao.flush()
            id = datanode.id
            self.sessao.rollback()
            print(id)
            return id
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


    def reset_status(self):
        try:
            self.sessao.query(DataNode).update({DataNode.status: 'Offline'})
            self.sessao.commit()
        except SQLAlchemyError as e:
            self.sessao.rollback()
            raise e

    def set_status(self, id, status):
        try:
            if status in ['Online', 'Offline', 'Busy']:
                datanode = self.get(id)
                datanode.status = status
                
                self.sessao.commit()
                return datanode
        except SQLAlchemyError as e:
            self.sessao.rollback()
            raise e

    def get_status(self, id):
        try:
            datanode = self.get(id)
            if datanode:
                return datanode.status
        except SQLAlchemyError as e:
            raise e
