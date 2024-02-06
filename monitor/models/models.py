from sqlalchemy import TIMESTAMP, Column, Enum, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

Base = declarative_base()

class DataNode(Base):
    __tablename__ = 'datanode'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    alias: Mapped[str] = mapped_column(String, unique=True)
    status: Mapped[str] = mapped_column(Enum('Online', 'Offline', 'Busy'), default='Online') # Online, Offline, Busy
    created_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
