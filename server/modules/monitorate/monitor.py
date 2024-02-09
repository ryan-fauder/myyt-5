from abc import ABC, abstractmethod

class AbstractMonitor(ABC):

    @abstractmethod
    def offer(self):
        pass

    @abstractmethod
    def store(self, alias: str):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

    @abstractmethod
    def check_alias(self, id: int, alias: str):
        pass

    @abstractmethod
    def check_online(self, id: int, alias: str):
        pass

    @abstractmethod
    def ping(self, id: int):
        pass
