import socket
from fileHelper import write_list, read_list
from environment import FILE_PATH, NETMASK

def connect(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)
    result = sock.connect_ex((hostname, port))
    sock.close()
    return result == 0

def search_hosts(netmask="192.168.1."):
    addresses = []
    for i in range(1,255):
        host = netmask+str(i)
        print(host)
        res = connect(host, 22)
        if res:
            print("Device found at: ", host + ":"+str(22))
            addresses.append(host)
    return addresses

if __name__ == '__main__':
    addresses = search_hosts(NETMASK)
    if addresses:
        success_flag = write_list(FILE_PATH, addresses)
        if success_flag:
            print("Endereços foram escritos com sucesso")
        else: 
            print("Não foi possível escrever no arquivo") 
    else:
        print('Nenhum endereço foi encontrado')