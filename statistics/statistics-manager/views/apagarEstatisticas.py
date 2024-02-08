from environment import STATISTICS_LOCATION
from services.fileHelper import deleteFilesFromPath
from controller import Controller

def apagarEstatisticas(controller: Controller):
    try:
        deleteFilesFromPath(STATISTICS_LOCATION)
        print("Todos os arquivos foram removidos.")
        controller.saved_statistics = {}
    except Exception as e:
        print(e)