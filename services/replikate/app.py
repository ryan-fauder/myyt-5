import sys
import subprocess
from fileHelper import read_list

def run_command(command: str):
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Comando executado: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python app.py $caminho_para_arquivo_de_enderecos")
        sys.exit(1)

    input_file_path = sys.argv[1]
    addresses = read_list(path=input_file_path)
    if not addresses:
        print("share-code (ERROR): Nenhum endereço foi encontrado no arquivo de endereços")
        sys.exit(1)
    
    run_command("chmod +x ./run.exp")
    run_command("chmod +x ./install.sh")
    for address in addresses:
        command = f"./run.exp {address} &"
        run_command(command)
