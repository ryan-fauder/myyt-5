from typing import TypedDict

class DataNodeDTO(TypedDict):
    id: int
    alias: str

class VideoDTO(TypedDict):
    id: int
    blob: bytes
    title: str
    description: str
    size: int