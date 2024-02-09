import time
from session import create_session
from dao.datanodeDAO import DataNodeDAO
from environment import INTERVAL_RESET_STATUS

def reset_status():
    while True:
        session = create_session()
        with DataNodeDAO(session) as datanode_dao:
            datanode_dao.reset_status()
            time.sleep(INTERVAL_RESET_STATUS)
