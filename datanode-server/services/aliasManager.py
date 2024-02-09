import os
from environment import ALIAS_FILE


def get_local_alias(monitorate):
    id, alias = None, None
    if os.path.exists(ALIAS_FILE):
        with open(ALIAS_FILE, 'r') as f:
            conteudo = f.read()
            try:
                id, alias = map(str.strip, conteudo.split(", "))
                id = int(id)
                if not monitorate.check_alias(id, alias):
                    print('INVALID ALIAS - aliasManager')
                    return None, None
            except ValueError:
                print('INVALID FILE FORMAT - aliasManager')
                return None, None
    return id, alias
def get_alias(monitorate):
    try:
        id, alias = get_local_alias(monitorate)
        if not id or not alias:
            id, alias = monitorate.register_datanode()
            if id and alias:
                with open(ALIAS_FILE, 'w') as f:
                    f.write(f"{id}, {alias}")
        return id, alias
    except:
        return None, None