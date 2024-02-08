from modules.statistikal import Statistikal

def registrarEstatistica(statistikal: Statistikal):
    topic = input("Informe o tópico: ")
    value = float(input("Informe o valor: "))
    author = input("Informe o autor: ")
    statistikal.register_statistic(topic, value, author)