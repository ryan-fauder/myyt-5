from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Video(Base):
    __tablename__ = 'videos'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    blob = Column(LargeBinary)
    size = Column(Integer)

    def dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "blob": self.blob,
            "size": self.size
        }
    