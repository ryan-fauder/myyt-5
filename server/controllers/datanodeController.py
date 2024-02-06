from dao.datanodeDAO import DataNodeDAO
from session import session
import rpyc

@rpyc.service
class DataNodeController(rpyc.Service):
    datanodeDAO = DataNodeDAO(session)
    @rpyc.exposed
    def store(self, id=None, alias=None):
        try:
            self.datanodeDAO.add(id=id, alias=alias)
            return True
        except: 
            return False
    @rpyc.exposed
    def delete(self, id=None):
        try:
            self.datanodeDAO.delete(id=id)
            return True
        except: 
            return False