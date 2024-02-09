import threading
from fakeclient import FakeClient
from environment import DOWNLOAD_PATH, UPLOAD_PATH

def upload_thread(client_id, file_path):
    fakeclient = FakeClient(client_id, DOWNLOAD_PATH, UPLOAD_PATH)
    print(f"Cliente {client_id} realizando upload do arquivo {UPLOAD_PATH}/{file_path}")
    fakeclient.upload(file_path)
    print(f"Upload do Cliente {client_id} concluído")

def download_thread(client_id, video_id):
    fakeclient = FakeClient(client_id, DOWNLOAD_PATH, UPLOAD_PATH)
    print(f"Cliente {client_id} realizando download do vídeo com ID {video_id}")
    fakeclient.download(video_id)
    print(f"Download do Cliente {client_id} concluído")

def main():
    fakeclient = FakeClient()
    num_clients = int(input("Digite a quantidade de clientes (padrão é 1): ") or 1)

    while True:
        print("\nOpções:")
        print("1. Fazer upload de um arquivo")
        print("2. Fazer download de um arquivo")
        print("3. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            file_path = input("Digite o caminho do arquivo: ")
            threads = [threading.Thread(target=upload_thread, args=(i+1, file_path)) for i in range(num_clients)]
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()

        elif choice == "2":
            videos = fakeclient.list()
            print("Vídeos disponíveis:")
            for i, video in enumerate(videos):
                print(f"{i + 1}. {video['title']}")

            index = int(input("Escolha o índice do vídeo para download: ")) - 1
            video_id = videos[index]['id']

            threads = [threading.Thread(target=download_thread, args=(i+1, video_id)) for i in range(num_clients)]
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()

        elif choice == "3":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
