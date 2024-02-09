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


# import rpyc_helper

# def display():
#     while True:
#         s = 0
#         for t in average_chunk_thoughtput:
#             s+=average_chunk_thoughtput[t]
#         print("Average chunk throughput =",s/len(average_chunk_thoughtput))
#         time.sleep(0.3)

# def download_video(thread_number):
#     database = rpyc_helper.connect("Database")

#     start_time = time.time()
#     chunk_start_time = time.time()
#     i=0
#     for chunk in database.file('FILE_51d9c78a-8182-4d05-b7e4-f3d3bcde3e25'):
#         #print("Thread",thread_number,"Received a chunk of len",len(chunk))
#         chunk_duration = time.time() - chunk_start_time
#         throughput = len(chunk)/chunk_duration
#         #print("Thread",thread_number,"Received a chunk of len",len(chunk),"current throughput =",throughput,"bytes/second")
#         if str(thread_number) not in average_chunk_thoughtput:
#             average_chunk_thoughtput[str(thread_number)] = 0
#         average_chunk_thoughtput[str(thread_number)] = average_chunk_thoughtput[str(thread_number)]*i/(i+1) + throughput/(i+1)
#         chunk_start_time = time.time()
#         i+=1

#     duration = time.time() - start_time
#     measured_time[str(thread_number)] = duration


# def main():
#     number_of_clients = 20

#     threads = []
#     for number in range(number_of_clients):
#         time.sleep(0.2)
#         thread = threading.Thread(target=download_video, args=(number,), name=f"Thread-{number}")
#         threads.append(thread)
#         thread.start()

#     display_thread = threading.Thread(target=display)
#     display_thread.start()

#     for thread in threads:
#         thread.join()

#     print("Todos os clientes já executaram")

# if __name__ == "__main__":
#     main()
