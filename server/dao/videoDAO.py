from models import Video
from sqlalchemy.orm import Session 
class VideoDAO:
    def __init__(self, session: Session):
        self.sessao = session

    def add(self, title, blob, size):
        new_video = Video(title=title, blob=blob, size=size)
        self.sessao.add(new_video)
        self.sessao.commit()
        return new_video.dict()
    
    def get(self, video_id):
        video = self.sessao.query(Video).filter_by(id=video_id).first()
        return video.dict()

    def delete(self, video_id):
        video = self.sessao.query(Video).filter_by(id=video_id).first()
        if video:
            self.sessao.delete(video)
            self.sessao.commit()
            return video.dict()
        
    def list(self):
        videos = self.sessao.query(Video.id, Video.title).all()
        return [
            {"id": id, "title": title}
            for (id, title) in videos
        ]
    
    def getByTitle(self, title):
        video = self.sessao.query(Video).filter_by(title=title).first()
        return video.dict()

if __name__ == "__main__":
    from ..session import session
    video_dao = VideoDAO(session)

    with open('./storage/video.mp4', 'rb') as arquivo:
        blob = arquivo.read()
        video_dao.add('Vídeo 1', blob, len(blob))
    
    with open('./storage/video2.mp4', 'rb') as arquivo:
        blob = arquivo.read()
        video_dao.add('Vídeo 2', blob, len(blob))

    video_id = 1
    video_obtido = video_dao.get(video_id)
    print(f"Vídeo obtido por ID {video_id}: {video_obtido.title}")

    video_a_remover = 2
    video_dao.delete(video_a_remover)
    print(f"Vídeo removido por ID {video_a_remover}")

    todos_os_videos = video_dao.list()
    print("Todos os vídeos no banco de dados:")
    for video in todos_os_videos:
        print(video.title)

    session.close()