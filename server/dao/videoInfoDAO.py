from sqlalchemy.orm import Session
from models import VideoInfo
from models import DataNode
from session import create_session

class VideoInfoDAO:
    def __init__(self, session: Session = None):
        if session is None:
            self.own_session = True
            self.sessao = create_session()
        else:
            self.own_session = False
            self.sessao = session

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.own_session:
            try:
                if exc_type is not None:
                    self.sessao.rollback()
                else:
                    self.sessao.commit()
            except Exception as e:
                print(f"Erro ao realizar commit ou rollback: {e}")
                self.sessao.rollback()
            finally:
                self.sessao.close()

    def add(self, title, description, size, commit=True, session=None):
        if session is None:
            session = self.sessao

        try:
            new_video = VideoInfo(title=title, description=description, size=size)
            session.add(new_video)

            if commit:
                session.commit()

            return new_video
        except Exception as e:
            print(f"Erro ao adicionar vídeo: {e}")
            if commit:
                self.sessao.rollback()

    def get(self, video_id, session=None):
        if session is None:
            session = self.sessao

        video = session.query(VideoInfo).filter_by(id=video_id).first()
        return video

    def delete(self, video_id, commit=True):
        try:
            video = self.sessao.query(VideoInfo).filter_by(id=video_id).first()
            if video:
                self.sessao.delete(video)

                if commit:
                    self.sessao.commit()

                return video
        except Exception as e:
            print(f"Erro ao excluir vídeo: {e}")
            if commit:
                self.sessao.rollback()
    def list(self):
        videos = self.sessao.query(VideoInfo).all()
        return videos

    def getByTitle(self, title):
        video = self.sessao.query(VideoInfo).filter_by(title=title).first()
        return video

    def associateDatanode(self, video_id: int, datanode: DataNode, commit=True):
        try:
            video = self.sessao.query(VideoInfo).filter_by(id=video_id).first()
            if video:
                video.datanodes.append(datanode)

                if commit:
                    self.sessao.commit()
        except Exception as e:
            if commit:
                print(f"Erro ao associar um datanode: {e}")
                self.sessao.rollback()

    def datanodes(self, video_id):
        video = self.sessao.query(VideoInfo).filter_by(id=video_id).first()
        return [(datanode.id, datanode.alias) for datanode in video.datanodes]
