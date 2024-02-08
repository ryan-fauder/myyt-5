import os

def deleteFilesFromPath(path: str):
    try:
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
    except Exception as e:
        print(f"Erro ao remover arquivos: {str(e)}")
        raise e