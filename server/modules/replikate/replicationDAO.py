
class ReplicationDAO:
    def __init__(self):
        self.hosts = [
            {"endereco": "192.168.1.1", "porta": 5000},
            {"endereco": "192.168.1.2", "porta": 5000},
        ]

    def get_hosts(self):
        return self.hosts
