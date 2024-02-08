import rpyc
import csv
import threading
import pandas as pd
from environment import STATISTICS_FILE_PATH, STATISTIC_ALIASES
lock = threading.Lock()
@rpyc.service
class StatisticController(rpyc.Service):
    ALIASES = [STATISTIC_ALIASES]

    @rpyc.exposed
    def register(self, topic, value, author):
        with lock:
            try:
                if not isinstance(topic, str) or not isinstance(value, (int, float)) or not isinstance(author, str):
                    raise ValueError("Parâmetros inválidos. Certifique-se de que topic é str, value é numérico e author é str.")
                with open(STATISTICS_FILE_PATH, 'a+', newline='', encoding='utf-8') as arquivo_csv:
                    writer = csv.writer(arquivo_csv)
                    writer.writerow((topic, value, author))
            except ValueError as ve:
                return f"Erro ao registrar estatísticas: {str(ve)}"
            except Exception as e:
                return f"Erro desconhecido ao registrar estatísticas: {str(e)}"

    @rpyc.exposed
    def retrieve(self):
        try:
            return pd.read_csv(STATISTICS_FILE_PATH, names=['Tópico', 'Valor', 'Autor']).values.tolist()
        except Exception as e:
            return f"Erro ao recuperar estatísticas: {str(e)}"
    @rpyc.exposed
    def reset(self):
        try:
            open(STATISTICS_FILE_PATH, 'w').close()
        except Exception as e:
            return f"Erro ao redefinir estatísticas: {str(e)}"