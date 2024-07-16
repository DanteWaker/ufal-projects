import socket
import threading
import sys

def enviar(sock, target_ip, target_port):
    while True:
        msg = input("")
        sock.sendto(msg.encode(), (target_ip, target_port))

def receber(sock):
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            print(f"Recebido de {addr}: {data.decode()}")
        except ConnectionResetError:
            print("Conexao perdida")
            continue

def start_udp_chat(port, target_ip, target_port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind(('0.0.0.0', port))
        print("Chat UDP iniciado")

        thread_send = threading.Thread(target=enviar, args=(s, target_ip, target_port))
        thread_receive = threading.Thread(target=receber, args=(s,))

        thread_send.start()
        thread_receive.start()

        thread_send.join()
        thread_receive.join()


# Professor, para iniciar o chat, o senhor precisa rodar o codigo, vim aqui, editar, e rodar o codigo editado em outro terminal
start_udp_chat(65001, '127.0.0.1', 65000)