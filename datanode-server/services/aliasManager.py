import os
from environment import ALIAS_FILE
from modules.monitorate import Monitorate

def get_local_alias(monitorate: Monitorate):
    try:
        if os.path.exists(ALIAS_FILE):
            with open(ALIAS_FILE, 'r') as file:
                content = file.read()
                id, local_alias = map(str.strip, content.split(", "))
                id = int(id)
                return id, local_alias
    except ValueError:
        print('ERRO: Formato de arquivo inválido - aliasManager')
    except Exception as e:
        print(f'ERRO: {e} - aliasManager')
    return None, None

def get_alias(monitorate: Monitorate):
    try:
        id, alias = get_local_alias(monitorate)

        if id and alias and monitorate.check_alias(id, alias):
            return id, alias

        id, alias = monitorate.register_datanode()
        if id and alias:
            with open(ALIAS_FILE, 'w') as file:
                file.write(f"{id}, {alias}")
        return id, alias
    except Exception as e:
        print(f'ERRO: {e} - aliasManager')
        return None, None
