from controller import Controller

def listarEstatistica(controller: Controller):
    print("\nEstatísticas Salvas:")
    for filename, _ in controller.saved_statistics.items():
        print(f"{filename}")