from modules.express.dispatcher import Dispatcher
from controllers.videoController import VideoController
from environment import HOST, PORT

host = HOST
port = PORT

dispatcher = Dispatcher(host, port)
router = dispatcher.Router()
router.get('/videos', VideoController.index)
router.post('/video', VideoController.store)
router.delete('/video', VideoController.delete)
router.post('/stream/id', VideoController.stream)
router.post('/video/id', VideoController.read)
router.post('/video/name', VideoController.readByTitle)
print(f"Servidor está escutando em {host}:{port}")
dispatcher.listen()