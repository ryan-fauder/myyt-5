import csv
import pandas as pd
import matplotlib.pyplot as plt
import threading

lock = threading.Lock()

def salvar_em_csv(tupla, nome_arquivo='dados.csv'):
    with lock:
        with open(nome_arquivo, 'a', newline='', encoding='utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(tupla)

def plotar_grafico_por_autor(nome_arquivo='dados.csv'):
    dados = pd.read_csv(nome_arquivo, names=['Tópico', 'Valor', 'Autor'])
    por_autor = dados.groupby('Autor')['Valor'].sum()

    por_autor.plot(kind='bar', rot=0)
    plt.title('Total por Autor')
    plt.xlabel('Autor')
    plt.ylabel('Total')
    plt.show()

def plotar_grafico_por_topico(nome_arquivo='dados.csv'):
    dados = pd.read_csv(nome_arquivo, names=['Tópico', 'Valor', 'Autor'])
    por_topico = dados.groupby('Tópico')['Valor'].sum()

    por_topico.plot(kind='bar', rot=0)
    plt.title('Total por Tópico')
    plt.xlabel('Tópico')
    plt.ylabel('Total')
    plt.show()

# Exemplo de uso
topico1 = ('Esporte', 10, 'Autor1')
topico2 = ('Tecnologia', 8, 'Autor2')

salvar_em_csv(topico1)
salvar_em_csv(topico2)

# Chamadas múltiplas com valores aleatórios
for _ in range(5):
    salvar_em_csv(('Esporte', 5+_, 'Autor1'))

for _ in range(5):
    salvar_em_csv(('Tecnologia', 3+_, 'Autor2'))

plotar_grafico_por_autor()
plotar_grafico_por_topico()
