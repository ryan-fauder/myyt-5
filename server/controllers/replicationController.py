from typing import Generator
from interfaces import VideoDTO
from dao.videoInfoDAO import VideoInfoDAO
from services.replicationService import ReplicationService
from session import create_session
from modules.playkite import AbstractPlaykite
import rpyc

@rpyc.service
class ReplicationController(rpyc.Service, AbstractPlaykite):
    @rpyc.exposed
    def store(self, body: VideoDTO):
        try:
            session = create_session()
            with VideoInfoDAO(session) as video_info_dao:
                title = body['title']
                description = body['description']
                size = body['size']
                video = video_info_dao.add(title, description, size)

                if not video:
                    return 'Um erro ocorreu na replicação: VideoInfo não pode ser criado'

                body['id'] = video.id
                response = ReplicationService.store(body)

                if response:
                    return video.dict()

        except Exception as e:
            print(f"Erro inesperado na replicação: {e}")
            raise e

    @rpyc.exposed
    def index(self):
        try:
            session = create_session()
            with VideoInfoDAO(session) as video_info_dao:
                videos = video_info_dao.list()
                response = [video.dict() for video in videos]
            return response

        except Exception as e:
            print(f"Erro inesperado ao obter lista de vídeos: {e}")
            raise

    @rpyc.exposed
    def delete(self, id: int):
        try:
            session = create_session()
            with VideoInfoDAO(session) as video_info_dao:
                ReplicationService.delete(id)
                video_deleted = video_info_dao.delete(id)

                if not video_deleted:
                    raise Exception('Um erro ocorreu na replicação: VideoInfo não pode ser removido')

                return video_deleted

        except Exception as e:
            print(f"Erro inesperado na replicação: {e}")
            raise e

    @rpyc.exposed
    def read(self, id: int):
        try:
            session = create_session()
            with VideoInfoDAO(session) as video_info_dao:
                video_info = video_info_dao.get(id)
                return video_info.dict() if video_info else None

        except Exception as e:
            print(f"Erro inesperado na replicação: {e}")
            raise e

    @rpyc.exposed
    def readByTitle(self, title: str):
        try:
            session = create_session()
            with VideoInfoDAO(session) as video_info_dao:
                video_info = video_info_dao.getByTitle(title)
                return video_info.dict() if video_info else None

        except Exception as e:
            print(f"Erro inesperado na replicação: {e}")
            raise e

    @rpyc.exposed
    def stream(self, id: int) -> Generator[bytes, None, None]:
        try:
            file_generator = ReplicationService.stream(id)
            return file_generator
        except Exception as e:
            print(f"Erro inesperado na replicação: {e}")
            raise e
