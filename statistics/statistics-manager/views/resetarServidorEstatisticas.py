from modules.statistikal import Statistikal
def resetarServidorEstatisticas(statistikal: Statistikal):
    print("\nTem certeza que deseja resetar as estatísticas?")
    print("1. Sim")
    print("0. Cancelar")

    choice = input("Escolha uma opção: ")

    if choice == '1':
        try:
            statistikal.reset_statistics()
            print("O servidor de estatísticas foi resetado com sucesso")
        except Exception as e:
            print(e)
    elif choice == '0':
        pass
    else:
        print("Opção inválida. Tente novamente.")