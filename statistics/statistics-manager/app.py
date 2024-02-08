from controller import Controller
from modules.statistikal import Statistikal
from views import *
from environment import STATISTICS_LOCATION
import sys
if __name__ == "__main__":
    statistikal = None

    while True:
        print("\nOpções:")
        print("1. Conectar ao serviço RPyC")
        print("0. Sair")
        choice = input("Escolha uma opção: ")
        if choice == '1':
            try:
                statistikal = Statistikal()
                print("Conectado com sucesso")
                break
            except Exception as e:
                print(e)
        if choice == '0':
            sys.exit(0)
        else:
            print("Opção inválida. Tente novamente.")
    controller = Controller(statistics_path=STATISTICS_LOCATION)
    while True:
        print("\nOpções:")
        print("2. Registrar estatística")
        print("3. Buscar e salvar estatísticas em arquivo")
        print("4. Exibir estatísticas")
        print("5. Listar estatísticas salvas")
        print("6. Apagar todas as estatísticas locais")
        print("7. Resetar servidor de estatistícas")
        print("0. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '2':
            registrarEstatistica(statistikal)
        elif choice == '3':
            salvarEstatistica(controller, statistikal)
        elif choice == '4':
            exibirEstatistica(controller)
        elif choice == '5':
            listarEstatistica(controller)
        elif choice == '6':
            apagarEstatisticas(controller)
        elif choice == '7':
            resetarServidorEstatisticas(statistikal)
        elif choice == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")