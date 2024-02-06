import rpyc

video = rpyc.connect_by_service('VIDEO_MANAGER_SERVER').root
videoMock = {
    "id": 2,
    "title": "Vídeo 2",
    "description": "Descrição Vídeo 2",
    "blob": b'BLOB',
    "size": 2000
}

video.store(videoMock)