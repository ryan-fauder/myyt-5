from abc import ABC, abstractmethod

class AbstractDataNoodle(ABC):

    @abstractmethod
    def store(self, id: str = None, alias: str = None):
        pass

    @abstractmethod
    def delete(self, id: str = None):
        pass