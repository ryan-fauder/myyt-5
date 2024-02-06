import time
from session import session
from dao.datanodeDAO import DataNodeDAO
from environment import INTERVAL_RESET_STATUS

def reset_status():
    datanode_dao = DataNodeDAO(session)
    while True:
        datanode_dao.reset_status()
        time.sleep(INTERVAL_RESET_STATUS)
