from models import Video
from session import create_session

class VideoDAO:
    def __init__(self, session=None):
        if session is None:
            self.sessao = create_session()
            self.own_session = True
        else:
            self.sessao = session
            self.own_session = False

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


    def add(self, id, title, description, path, size, commit=True):
        try:
            new_video = Video(id=id, title=title, description=description, path=path, size=size)
            self.sessao.add(new_video)
            if commit:
                self.sessao.commit()
            return new_video
        except Exception as e:
            print(f"Erro ao adicionar vídeo: {e}")
            if commit:
                self.sessao.rollback()

    def get(self, video_id):
        video = self.sessao.query(Video).filter_by(id=video_id).first()
        return video

    def delete(self, video_id, commit=True):
        try:
            video = self.sessao.query(Video).filter_by(id=video_id).first()
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
        videos = self.sessao.query(Video.id, Video.title, Video.description, Video.size, Video.created_at).all()
        return videos

    def getByTitle(self, title):
        video = self.sessao.query(Video).filter_by(title=title).first()
        return video if video else None

if __name__ == "__main__":
    session = create_session()
    with VideoDAO(session) as video_dao:
        with open('./storage/video.mp4', 'rb') as arquivo:
            blob = arquivo.read()
            video_dao.add('Vídeo 1', blob, len(blob))

        with open('./storage/video2.mp4', 'rb') as arquivo:
            blob = arquivo.read()
            video_dao.add('Vídeo 2', blob, len(blob))

        video_id = 1
        video_obtido = video_dao.get(video_id)
        print(f"Vídeo obtido por ID {video_id}: {video_obtido['title']}")

        video_a_remover = 2
        video_dao.delete(video_a_remover)
        print(f"Vídeo removido por ID {video_a_remover}")

        todos_os_videos = video_dao.list()
        print("Todos os vídeos no banco de dados:")
        for video in todos_os_videos:
            print(video['title'])