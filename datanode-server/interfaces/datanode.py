from typing import TypedDict

class DataNodeDTO(TypedDict):
    id: int
    status: str
    host: str
    port: int

class VideoDTO(TypedDict):
    id: int
    blob: bytes
    title: str
    description: str
    size: int