import socket
import threading
from replicationDAO import ReplicationDAO
class ReplicationService:
    def __init__(self, replication_dao):
        self.replication_dao = replication_dao

    def listen(self, porta):
        servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor_socket.bind(("localhost", porta))
        servidor_socket.listen(5)

        print(f"O ReplicationService está ouvindo em localhost:{porta}")

        while True:
            cliente_socket, endereco_cliente = servidor_socket.accept()
            print(f"Conexão recebida de {endereco_cliente}")

            # Cria uma nova thread para lidar com a conexão
            thread = threading.Thread(target=self.replicar, args=(cliente_socket,))
            thread.start()

    def replicar(self, cliente_socket):
        # Lógica para receber e armazenar a replicação
        # (Implemente conforme necessário)
        # Aqui, você pode chamar métodos como selectHost para escolher hosts e
        # enviar a replicação para outros computadores usando o método reply.

        # Exemplo: Obtendo a lista de hosts do ReplicationDAO
        hosts = self.replication_dao.get_hosts()

        # Exemplo: Selecionando um host para a replicação
        host_destino = self.selectHost(hosts)

        # Exemplo: Enviando a replicação para o host selecionado
        self.reply(host_destino, "Dados de replicação")

        # Fechando o socket do cliente após a replicação
        cliente_socket.close()

    def reply(self, host_destino, dados_replicacao):
        # Lógica para enviar a replicação para outro computador
        # (Implemente conforme necessário)
        print(f"Enviando replicação para {host_destino['endereco']}:{host_destino['porta']}")
        # Aqui você pode usar sockets para enviar dados para o host de destino

    def selectHost(self, hosts):
        # Lógica para selecionar um host para a replicação
        # (Implemente conforme necessário)
        # Aqui, você pode adicionar lógica para escolher hosts com base em critérios específicos.
        return hosts[0]  # Exemplo simples: retorna o primeiro host da lista

if __name__ == "__main__":
    # Exemplo de uso
    replication_dao = ReplicationDAO()
    replication_service = ReplicationService(replication_dao)
    replication_service.listen(8888)
