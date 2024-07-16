import grpc
import time_sync_pb2
import time_sync_pb2_grpc
from colorama import Fore, Style, init
import time

# Inicializa o Colorama
init(autoreset=True)

def log(message, color=Fore.WHITE, style=Style.NORMAL):
    """Função auxiliar para registrar mensagens com estilo."""
    print(f"{color}{style}{message}{Style.RESET_ALL}")

def register_client(stub, client_id):
    try:
        # Tenta registrar o cliente no servidor
        stub.RegisterClient(time_sync_pb2.RegisterClientRequest(client_id=client_id))
        log(f"Registrado no servidor com o ID: {client_id}", Fore.GREEN, Style.BRIGHT)
    except grpc.RpcError as e:
        log(f"Falha ao registrar no servidor: {e}", Fore.RED, Style.BRIGHT)

def stream_time_updates(stub):
    try:
        for time_update in stub.StreamTimeUpdates(time_sync_pb2.Empty()):
            formatted_time = Style.BRIGHT + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_update.seconds)) + f".{time_update.milliseconds:03}ms"
            log(f"[{formatted_time}] 🔄 Recebida atualização de tempo: {formatted_time}.", Fore.GREEN, Style.BRIGHT)
    except grpc.RpcError as e:
        log(f"Falha na conexão de stream: {e}", Fore.RED, Style.BRIGHT)

def main():
    client_id = "client_1"  # Este ID deve ser único para cada cliente
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = time_sync_pb2_grpc.TimeSyncServiceStub(channel)
        
        # Tenta registrar o cliente no servidor
        log(f"Tentando registrar o cliente com ID: {client_id}...", Fore.CYAN, Style.BRIGHT)
        register_client(stub, client_id)
        
        # Inicia o streaming de atualizações de tempo
        log("Iniciando streaming de atualizações de tempo...", Fore.CYAN, Style.BRIGHT)
        stream_time_updates(stub)

if __name__ == '__main__':
    main()
