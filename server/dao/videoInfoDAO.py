from sqlalchemy.orm import Session
from models import VideoInfo
from models.models import DataNode

class VideoInfoDAO:
    def __init__(self, session: Session):
        self.sessao = session

    def add(self, title, description, size):
        try:
            new_video = VideoInfo(title=title, description=description, size=size)
            self.sessao.add(new_video)
            self.sessao.commit()
            return new_video
        except Exception as e:
            self.sessao.rollback()
    def get(self, video_id):
        video = self.sessao.query(VideoInfo).filter_by(id=video_id).first()
        return video

    def delete(self, video_id):
        try:
            video = self.sessao.query(VideoInfo).filter_by(id=video_id).first()
            if video:
                self.sessao.delete(video)
                self.sessao.commit()
                return video
        except Exception as e:
            self.sessao.rollback()
    def list(self):
        videos = self.sessao.query(VideoInfo).all()
        return videos
    
    def getByTitle(self, title):
        video = self.sessao.query(VideoInfo).filter_by(title=title).first()
        return video

    def associateDatanode(self, video_id, datanode):
        try:
            video = self.sessao.query(VideoInfo).filter_by(id=video_id).first()
            if(video):
                video.datanodes.append(datanode)
                self.sessao.commit()
        except Exception as e:
            self.sessao.rollback()

    def datanodes(self, video_id):
        video = self.sessao.query(VideoInfo).filter_by(id=video_id).first()
        return [(datanode.id, datanode.alias) for datanode in video.datanodes]
if __name__ == "__main__":
    from session import session
    video_dao = VideoInfoDAO(session)
    videoMock = {
        "title": "Vídeo 1",
        "description": "Descrição Vídeo 1",
        "size": 1000
    }
    print('Starting test')
    video_dao.add(videoMock['title'], videoMock['description'], videoMock['size'])

    videoMock = {
        "title": "Vídeo 2",
        "description": "Descrição Vídeo 2",
        "size": 2000
    }

    video_obtido2 = video_dao.add(videoMock['title'], videoMock['description'], videoMock['size']).dict()
    print(video_obtido2)
    video = video_dao.get(video_obtido2['id']).dict()
    print(f"Vídeo obtido por ID {video['id']}: {video['title']}")

    video_removido = video_dao.delete(video['id']).dict()
    print(f"Vídeo removido por ID {video_removido}")

    todos_os_videos = video_dao.list()
    print("Todos os vídeos no banco de dados:")
    for videoModel in todos_os_videos:
        video = videoModel.dict()
        print(video['id'])
        print(video['title'])
        print(video['description'])
    session.close()