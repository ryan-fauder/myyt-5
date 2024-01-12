from modules.message import Request, Response
from dao.videoDAO import VideoDAO
from session import session

class VideoController:
    videoDAO = VideoDAO(session)
    def store(request: Request) -> Response:
        body = request.data
        title, blob, size = body['title'], body['blob'], body['size']
        new_video = VideoController.videoDAO.add(title, blob, size)
        del new_video['blob']
        return Response('200', new_video)
    def index(request: Request) -> Response:
        videos = VideoController.videoDAO.list()
        return Response('200', videos)
    def delete(request: Request) -> Response:
        body = request.data
        id = body['id']
        video_deleted = VideoController.videoDAO.delete(id)
        del video_deleted['blob']
        return Response('200', video_deleted)
    def read(request: Request) -> Response:
        body = request.data
        id = body['id']
        video = VideoController.videoDAO.get(id)
        del video['blob']
        return Response('200', video)
    def readByTitle(request: Request) -> Response:
        body = request.data
        title = body['title']
        video = VideoController.videoDAO.getByTitle(title)
        del video['blob']
        return Response('200', video)
    def stream(request: Request) -> Response:
        body = request.data
        id = body['id']
        video = VideoController.videoDAO.get(id)
        blob = video['blob']
        return Response('200', blob)