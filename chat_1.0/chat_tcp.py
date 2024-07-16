import socket
import threading
import sys

def enviar(sock):
    while True:
        msg = input("")
        sock.sendall(msg.encode())

def receber(sock):
    while True:
        data = sock.recv(1024)
        if not data:
            break
        print(f"Received: {data.decode()}")

def iniciar_servidor(porta):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', porta))
    server.listen(1)
    conn, addr = server.accept()
    return conn

def iniciar_chat(ip, porta, modo):
    sock = None
    if modo == 'server':
        sock = iniciar_servidor(porta)
    elif modo == 'client':
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, porta))
        print("Chat iniciado")

    thread_send = threading.Thread(target=enviar, args=(sock,))
    thread_receive = threading.Thread(target=receber, args=(sock,))

    thread_send.start()
    thread_receive.start()

    thread_send.join()
    thread_receive.join()

def main():
    if len(sys.argv) != 4:
        print("Como usar: python tcp_chat.py [ip] [porta] [modo]")
        return

    ip = sys.argv[1]
    porta = int(sys.argv[2])
    modo = sys.argv[3]

    if modo not in ['server', 'client']:
        print("Precisa ser 'server' ou 'client'")
        return

    iniciar_chat(ip, porta, modo)

if __name__ == "__main__":
    main()
