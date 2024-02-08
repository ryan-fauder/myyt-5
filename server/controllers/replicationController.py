from dao.datanodeDAO import DataNodeDAO
from interfaces.datanode import VideoDTO
from dao.videoInfoDAO import VideoInfoDAO
from services.replicationService import ReplicationService
from session import session
import rpyc

@rpyc.service
class ReplicationController(rpyc.Service):
    videoInfoDAO = VideoInfoDAO(session)
    datanodeDAO = DataNodeDAO(session)
    @rpyc.exposed
    def store(self, body: VideoDTO):
        title = body['title']
        description = body['description']
        size = body['size']
        video = ReplicationController.videoInfoDAO.add(title, description, size)
        if not video: return 'Um erro ocorreu na replicação: VideoInfo não pode ser criado'
        body['id'] = video.id
        response = ReplicationService.store(body)
        if(response):
            return video.dict()
    @rpyc.exposed
    def index(self):
        videos = ReplicationController.videoInfoDAO.list()
        response = [
            video.dict()
            for video in videos
        ]
        return response
    @rpyc.exposed
    def delete(self, id: int):
        ReplicationService.delete(id)
        video_deleted = ReplicationController.videoInfoDAO.delete(id)
        if not video_deleted: return 'Um erro ocorreu na replicação: VideoInfo não pode ser criado'
        return video_deleted
    @rpyc.exposed
    def read(self, id: int):
        videoInfo = ReplicationController.videoInfoDAO.get(id)
        return videoInfo.dict()
    @rpyc.exposed
    def readByTitle(self, title: str):
        video = ReplicationController.videoInfoDAO.getByTitle(title)
        return video
    @rpyc.exposed
    def stream(self, id: int):
        blob = ReplicationService.stream(id)
        return blob