from controller import Controller
from services.plotHelper import *

def exibirEstatistica(controller: Controller):
    print("\nOpções de Exibição:")
    print("1. Por arquivo")
    print("2. Geral por tópico")
    print("0. Voltar")

    display_choice = input("Escolha uma opção de exibição: ")
    if display_choice == '1':
        filename = input("Informe o nome do arquivo: ")
        statistics = controller.saved_statistics.get(filename)
        dataframe = pd.DataFrame(statistics, columns=['Tópico', 'Valor', 'Autor'])
        print(dataframe)
        if statistics:
            print("\nOpções de Exibição por Arquivo:")
            print("1. Por Tópico")
            print("2. Por Tópico e Autor")
            print("0. Voltar")
            file_display_choice = input("Escolha uma opção de exibição por arquivo: ")
            if file_display_choice == '1':
                    plot_statistics_by_topic(dataframe)
            elif file_display_choice == '2':
                    plot_statistics_by_topic_and_author(dataframe)
            elif file_display_choice == '0':
                pass
            else:
                print("Opção inválida. Tente novamente.")
        else:
            print(f"Arquivo '{filename}' não encontrado. Busque as estatísticas primeiro.")
    elif display_choice == '2':
        statistics = controller.saved_statistics
        dataframe = pd.DataFrame([(file, topic, value, author) for file, data in statistics.items() for topic, value, author in data],
                columns=['Arquivo', 'Tópico', 'Valor', 'Autor'])
        plot_general_statistics_by_topic(dataframe)
    elif display_choice == '0':
        pass
    else:
        print("Opção inválida. Tente novamente.")