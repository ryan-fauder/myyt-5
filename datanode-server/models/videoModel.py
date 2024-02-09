from sqlalchemy import TIMESTAMP, Column, DateTime, Enum, Integer, String, LargeBinary, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

Base = declarative_base()

class Video(Base):
    __tablename__ = 'videos'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=True, default='')
    description: Mapped[str] = mapped_column(String, nullable=True, default='')
    size: Mapped[int] = mapped_column(Integer, default=0)
    path: Mapped[str] = mapped_column(String, default='')
    created_at: Mapped[str] = mapped_column(DateTime(timezone=True), default=func.now(), server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
  
    def dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at.strftime("%m/%d/%Y"),
            "size": self.size
        }