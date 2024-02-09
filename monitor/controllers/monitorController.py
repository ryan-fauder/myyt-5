from dao.datanodeDAO import DataNodeDAO
from environment import DATANOODLE_MANAGER_ALIASES
from modules.datanoodle import Datanoodle
from modules.monitorate import AbstractMonitor
from session import create_session
import rpyc

@rpyc.service
class MonitorController(rpyc.Service, AbstractMonitor):
    ALIASES = ["MONITOR_SERVER"]

    def connects_datanode_manager(self):
        try:
            return Datanoodle(DATANOODLE_MANAGER_ALIASES)
        except Exception as e:
            raise e

    @rpyc.exposed
    def offer(self):
        try:
            session = create_session()
            with DataNodeDAO(session) as datanode_dao:
                id = datanode_dao.next_id()
                return f"PLAYKITE_{id}"
        except Exception as e:
            raise e
    
    @rpyc.exposed
    def store(self, alias: str):
        try:
            session = create_session()
            with DataNodeDAO(session) as datanode_dao:
                datanoodle = self.connects_datanode_manager()

                datanode = datanode_dao.add(alias=alias)
                if not datanode:
                    print("Falha ao adicionar um datanode em MonitorController")
                    return None

                ack = datanoodle.register_datanode(id=datanode.id, alias=datanode.alias)
                if not ack:
                    print("Falha ao adicionar um datanode ao DataManagerServer em MonitorController")
                    return None

                return datanode.id, datanode.alias
        except Exception as e:
            raise e

    @rpyc.exposed
    def delete(self, id: int):
        try:
            session = create_session()
            with DataNodeDAO(session) as datanode_dao:
                datanoodle = self.connects_datanode_manager()

                datanode = datanode_dao.delete(id)
                if datanode:
                    while True:
                        if datanoodle.delete_datanode(id=id):
                            break
                return datanode
        except Exception as e:
            raise e

    @rpyc.exposed
    def check_alias(self, id: int, alias: str):
        try:
            session = create_session()
            with DataNodeDAO(session) as datanode_dao:
                datanode = datanode_dao.find(alias=alias)
                if not datanode:
                    return None
                return datanode.id == id
        except Exception as e:
            raise e

    @rpyc.exposed
    def check_online(self, id: int, alias: str):
        try:
            session = create_session()
            with DataNodeDAO(session) as datanode_dao:
                datanode = datanode_dao.find(alias=alias)
                if not datanode:
                    return None
                return datanode.id == id and datanode.status == 'Online'
        except Exception as e:
            raise e

    @rpyc.exposed
    def ping(self, id: int):
        try:
            session = create_session()
            with DataNodeDAO(session) as datanode_dao:
                datanode = datanode_dao.set_status(id, 'Online')
                return datanode.status
        except Exception as e:
            raise e
