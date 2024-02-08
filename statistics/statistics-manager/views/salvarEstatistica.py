from controller import Controller
from modules.statistikal import Statistikal

def salvarEstatistica(controller: Controller, statistikal: Statistikal):
    filename = input("Informe o nome do arquivo para salvar as estatísticas: ")
    statistics = statistikal.retrieve_statistics()
    if statistics:
        controller.save_statistics_to_file(filename, statistics)
