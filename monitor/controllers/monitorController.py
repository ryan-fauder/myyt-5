
from dao.datanodeDAO import DataNodeDAO
from environment import REPLIKATE_DATANODE_MANAGER_ALIASES
from modules.replikate import Replikate
from session import session
import rpyc

@rpyc.service
class MonitorController(rpyc.Service):
    ALIASES = ["MONITOR_SERVER"]
    datanodeDAO = DataNodeDAO(session)
    replikate: Replikate = None
    def connects_datanode_manager(self):
        return Replikate(REPLIKATE_DATANODE_MANAGER_ALIASES)
    @rpyc.exposed
    def offer(self):
        # Offering a Alias
        id = MonitorController.datanodeDAO.next_id()
        return f"DATANODE_{id}"
    def store(self, alias):
        if not self.replikate:
            self.replikate = self.connects_datanode_manager()
        datanode = MonitorController.datanodeDAO.add(alias=alias)
        if not datanode:
            print("Falha ao adicionar um datanode em MonitorController")
            return None
        ack = self.replikate.register_datanode(id=datanode.id, alias=datanode.alias)
        if not ack:
            print("Falha ao adicionar um datanode ao DataManagerServer em MonitorController")
            return None
        return datanode.id, datanode.alias
    @rpyc.exposed
    def delete(self, id: int):
        if not self.replikate:
            self.replikate = self.connects_datanode_manager()
        datanode = MonitorController.datanodeDAO.delete(id)
        if datanode:
            while True:
                if self.replikate.delete_datanode(id=id):
                    break
        return datanode
    @rpyc.exposed
    def check_alias(self, id, alias):
        datanode = MonitorController.datanodeDAO.find(alias=alias)
        if not datanode:
            return None
        return datanode.id == id
    @rpyc.exposed
    def check_online(self, id, alias):
        datanode = MonitorController.datanodeDAO.find(alias=alias)
        if not datanode:
            return None
        return datanode.id == id and datanode.status == 'Online'
    @rpyc.exposed
    def ping(self, id: int):
        datanode = MonitorController.datanodeDAO.set_status(id, 'Online')
        return datanode.status