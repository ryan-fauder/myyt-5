import rpyc
from dao.videoDAO import VideoDAO
from modules.multer import Multer
from modules.playkite import AbstractPlaykite
from session import create_session
from environment import UPLOAD_FILE_PATH

@rpyc.service
class VideoController(rpyc.Service, AbstractPlaykite):
    multer = Multer(UPLOAD_FILE_PATH)
    
    @rpyc.exposed
    def store(self, id, title, description, file_generator, size):
        try:
            session = create_session()
            with VideoDAO(session) as dao:
                path = self.multer.write_file(file_generator)
                new_video = dao.add(id, title, description, path, size)
                return new_video.dict()
        except Exception as e:
            raise e

    @rpyc.exposed
    def index(self):
        session = create_session()
        with VideoDAO(session) as dao:
            videos = dao.list()
            return [
                {"id": id, "title": title, "description": description, "size": size, "created_at": created_at.strftime("%m/%d/%Y")}
                for (id, title, description, size, created_at) in videos
            ]

    @rpyc.exposed
    def delete(self, id):
        session = create_session()
        with VideoDAO(session) as dao:
            video_deleted = dao.delete(id)
            self.multer.remove_file(video_deleted.path)
            return video_deleted.dict()

    @rpyc.exposed
    def read(self, id):
        session = create_session()
        with VideoDAO(session) as dao:
            video = dao.get(id)
            return video.dict()

    @rpyc.exposed
    def readByTitle(self, title):
        session = create_session()
        with VideoDAO(session) as dao:
            video = dao.getByTitle(title)
            return video.dict()

    @rpyc.exposed
    def stream(self, id):
        session = create_session()
        with VideoDAO(session) as dao:
            video = dao.get(id)
            file_generator = self.multer.read_file(video.path)
            return file_generator            
