from dao.videoDAO import VideoDAO
from session import session
import rpyc

@rpyc.service
class VideoController(rpyc.Service):
    videoDAO = VideoDAO(session)

    @rpyc.exposed
    def store(self, id, title, description, blob, size):
        new_video = VideoController.videoDAO.add(id, title, description, blob, size)
        del new_video['blob']
        return new_video
    
    @rpyc.exposed
    def index(self):
        videos = VideoController.videoDAO.list()
        return videos
    
    @rpyc.exposed
    def delete(self, id):
        video_deleted = VideoController.videoDAO.delete(id)
        del video_deleted['blob']
        return video_deleted
    
    @rpyc.exposed
    def read(self, id):
        video = VideoController.videoDAO.get(id)
        del video['blob']
        return video
    
    @rpyc.exposed
    def readByTitle(self, title):
        video = VideoController.videoDAO.getByTitle(title)
        del video['blob']
        return video
    
    @rpyc.exposed
    def stream(self, id):
        video = VideoController.videoDAO.get(id)
        blob = video['blob']
        return blob