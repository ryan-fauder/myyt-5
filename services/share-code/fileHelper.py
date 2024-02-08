
def write_list(path: str, list: list[str]):
    try:
        with open(path, 'w') as file:
            for item in list:
                file.write(f"{item}\n")
        return True
    except FileNotFoundError:
        print(f"O arquivo '{path}' não foi encontrado.")
        return False
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return False
def read_list(path: str) -> list[str]:
    
    try:
        with open(path, 'r') as file:
            items = file.readlines()
        items = [item.strip() for item in items]
        return items
    except FileNotFoundError:
        print(f"O arquivo '{path}' não foi encontrado.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return []