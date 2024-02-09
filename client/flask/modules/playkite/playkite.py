from abc import ABC, abstractmethod
from typing import Generator
from .interfaces import VideoDTO

class AbstractPlaykite(ABC):

    @abstractmethod
    def store(self, body: VideoDTO) -> VideoDTO:
        pass

    @abstractmethod
    def index(self) -> VideoDTO:
        pass

    @abstractmethod
    def delete(self, id: int) -> VideoDTO:
        pass

    @abstractmethod
    def read(self, id: int) -> VideoDTO:
        pass

    @abstractmethod
    def readByTitle(self, title: str) -> VideoDTO:
        pass

    @abstractmethod
    def stream(self, id: int) -> Generator[bytes, None, None]:
        pass
