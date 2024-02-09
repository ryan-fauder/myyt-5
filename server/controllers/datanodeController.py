from dao.datanodeDAO import DataNodeDAO
from session import create_session
from modules.datanoodle import AbstractDataNoodle
import rpyc

@rpyc.service
class DataNodeController(rpyc.Service, AbstractDataNoodle):
    @rpyc.exposed
    def store(self, id=None, alias=None):
        try:
            if id is None or alias is None:
                raise ValueError("Parâmetros 'id' e 'alias' são obrigatórios para a operação de armazenamento.")
            session = create_session()
            with DataNodeDAO(session) as datanode_dao:
                datanode_dao.add(id=id, alias=alias)

            return True
        except ValueError as ve:
            print(f"Falha ao armazenar datanode: {ve}")
            raise ve
        except Exception as e:
            print(f"Erro inesperado ao armazenar datanode: {e}")
            raise e

    @rpyc.exposed
    def delete(self, id=None):
        try:
            if id is None:
                raise ValueError("Parâmetro 'id' é obrigatório para a operação de exclusão.")
            session = create_session()
            with DataNodeDAO(session) as datanode_dao:
                datanode_dao.delete(id=id)

            return True
        except ValueError as ve:
            print(f"Falha ao excluir datanode: {ve}")
            raise ve
        except Exception as e:
            print(f"Erro inesperado ao excluir datanode: {e}")
            raise e
