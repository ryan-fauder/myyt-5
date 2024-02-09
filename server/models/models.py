import datetime
from typing import List
from sqlalchemy import TIMESTAMP, Column, DateTime, Enum, Integer, String, LargeBinary, func
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Table, ForeignKey, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

Base = declarative_base()

datanode_videoinfo_association = Table(
    "datanode_videoinfo_association",
    Base.metadata,
    Column("datanode_id", ForeignKey("datanode.id"), primary_key=True),
    Column("videoinfo_id", ForeignKey("videoinfo.id"), primary_key=True),
)

class DataNode(Base):
    __tablename__ = 'datanode'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    alias: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(Enum('Online', 'Offline', 'Busy'), default='Online') # Online, Offline, Busy
    videoinfos: Mapped[List["VideoInfo"]] = relationship(
        secondary=datanode_videoinfo_association, back_populates="datanodes"
    )
    def dict(self) -> dict:
        return {
            "id": self.id,
            "alias": self.alias,
        }
class VideoInfo(Base):
    __tablename__ = 'videoinfo'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    size: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[str] = mapped_column(DateTime(timezone=True), default=func.now(), server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    datanodes: Mapped[List["DataNode"]] = relationship(
        secondary=datanode_videoinfo_association, back_populates="videoinfos"
    )
    def dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at.strftime("%m/%d/%Y"),
            "size": self.size
        }







