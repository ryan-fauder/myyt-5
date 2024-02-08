import csv
import os
class Controller:
    statistics_path = ''

    def __init__(self, statistics_path: str):
        self.statistics_path = statistics_path
        self.saved_statistics = self.load_saved_statistics()
    
    def load_saved_statistics(self):
        saved_statistics = {}
        for filename in os.listdir(self.statistics_path):
            if filename.endswith(".csv"):
                file_path = os.path.join(self.statistics_path, filename)
                base_name = os.path.splitext(filename)[0]
                with open(file_path, 'r', newline='', encoding='utf-8') as file_csv:
                    reader = csv.reader(file_csv)
                    statistics = [(item[0], float(item[1]), item[2]) for item in reader]
                    saved_statistics[base_name] = statistics
        return saved_statistics
    
    def save_statistics_to_file(self, filename, statistics):
        try:
            path = f"{self.statistics_path}/{filename}.csv"
            with open(path, 'w', newline='', encoding='utf-8') as file_csv:
                writer = csv.writer(file_csv)
                writer.writerows(statistics)
            print(f"Estatísticas salvas em '{filename}'")
            self.saved_statistics[filename] = statistics
        except Exception as e:
            print(f"Erro ao salvar estatísticas em arquivo: {str(e)}")
