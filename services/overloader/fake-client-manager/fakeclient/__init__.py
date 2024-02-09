import time
from .modules.playkite import Playkite, VideoDTO
from .modules.statistikal import Statistikal
from .modules.multer import Multer
from .environment import PLAYKITE_VIDEO_MANAGER_ALIASES

class FakeClient():
    def __init__(self, id = None, download_path='./downloads', upload_path = './uploads') -> None:
        self.download_path = download_path
        self.upload_path = upload_path
        self.statistikal: Statistikal = None
        self.id = id
        pass
    def set_id(self, id):
        self.id = id
    def upload(self, filename) -> VideoDTO:
        try:
            playkite = Playkite(PLAYKITE_VIDEO_MANAGER_ALIASES)
            multer = Multer(self.upload_path)
            file_generator = multer.read_file(filename, self.id)

            video: VideoDTO = {
                "title": f"VIDEO_{self.id}",
                "file_generator": file_generator,
                "description": "Video Fake Client",
                "size": 0
            }

            start_time = time.time()
            video_stored = playkite.store_video(video)
            measured_time = time.time() - start_time
            self.statistikal = Statistikal()
            self.statistikal.register_statistic('upload_time', float(measured_time), str(self.id))
            
            return video_stored
        except Exception as e:
            raise e

    def download(self, video_id) -> None:
        try:
            playkite = Playkite(PLAYKITE_VIDEO_MANAGER_ALIASES)
            multer = Multer(self.download_path)
            file_generator = playkite.stream_video(video_id)
            
            start_time = time.time()
            multer.write_file(file_generator, self.id)
            measured_time = time.time() - start_time
            self.statistikal = Statistikal()
            self.statistikal.register_statistic('download_time', float(measured_time), str(self.id))
        except Exception as e:
            raise e
    def list(self) -> None:
        try:
            playkite = Playkite(PLAYKITE_VIDEO_MANAGER_ALIASES)
            return playkite.index_videos()
        except Exception as e:
            raise e
fakeclient = FakeClient()