import matplotlib.pyplot as plt
import pandas as pd

def plot_statistics_by_topic(dataframe: pd.DataFrame):
    try:
        grouped_data = dataframe.groupby('Tópico')['Valor'].mean().reset_index()

        plt.figure(figsize=(10, 6))
        plt.bar(grouped_data['Tópico'], grouped_data['Valor'])
        plt.xlabel('Tópico')
        plt.ylabel('Valor Médio')
        plt.title(f'Valores Médios por Tópico')
        plt.show()
    except Exception as e:
        print(f"Erro ao plotar estatísticas por tópico: {str(e)}")


def plot_statistics_by_topic_and_author(dataframe: pd.DataFrame):
    try:
        grouped_data = dataframe.groupby(['Tópico', 'Autor']).mean().reset_index()

        for topic, group in grouped_data.groupby('Tópico'):
            plt.figure(figsize=(10, 6))
            plt.bar(group['Autor'], group['Valor'], label=topic)
            plt.xlabel('Autor')
            plt.ylabel('Valor Médio')
            plt.title(f'Estatísticas por Tópico e Autor - {topic}')
            plt.legend()
            plt.show()
    except Exception as e:
        print(f"Erro ao plotar estatísticas por tópico e autor: {str(e)}")

def plot_general_statistics_by_topic(dataframe: pd.DataFrame):
    try:
        averages_by_file_and_topic = dataframe.groupby(['Arquivo', 'Tópico'])['Valor'].mean().unstack()

        fig, ax = plt.subplots()
        averages_by_file_and_topic.plot(kind='bar', ax=ax)

        ax.set_xlabel('Arquivos')
        ax.set_ylabel('Média dos Valores por Tópico')
        ax.set_title('Média dos Valores por Tópico em Cada Arquivo')
        ax.legend(title='Tópico', bbox_to_anchor=(1.05, 1), loc='upper left')

        plt.show()
    except Exception as e:
        print(f"Erro ao plotar estatísticas gerais por tópico: {str(e)}")


if __name__ == '__main__':
    data = [
        ('Topic1', 10.0, 'Author1'),
        ('Topic1', 15.0, 'Author2'),
        ('Topic1', 12.0, 'Author1'),
        ('Topic2', 25.0, 'Author2'),
        ('Topic2', 30.0, 'Author1'),
        ('Topic2', 28.0, 'Author2'),
    ]
    # Criar DataFrame a partir dos dados
    df = pd.DataFrame(data, columns=['Tópico', 'Valor', 'Autor'])
    print(df)
    plot_statistics_by_topic(df)
    plot_statistics_by_topic_and_author(df)