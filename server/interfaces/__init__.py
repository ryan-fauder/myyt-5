from typing import Generator, Optional, TypedDict

class DataNodeDTO(TypedDict):
    id: int
    alias: str

class VideoDTO(TypedDict):
    id: int
    title: str
    description: str
    size: int
    file_generator: Optional[Generator[bytes, None, None]]