from concurrent import futures
import time
import grpc
from colorama import Fore, Style, init
import time_sync_pb2
import time_sync_pb2_grpc
import threading

# Inicializa o Colorama
init(autoreset=True)

def log(message, color=Fore.WHITE, style=Style.NORMAL):
    """Função auxiliar para registrar mensagens com estilo."""
    print(f"{color}{style}{message}{Style.RESET_ALL}")

class TimeSyncService(time_sync_pb2_grpc.TimeSyncServiceServicer):
    def __init__(self):
        self.clients_lock = threading.Lock()
        self.clients = []

    def RegisterClient(self, request, context):
        with self.clients_lock:
            self.clients.append(context)
            log(f"🆕 Cliente registrado: {request.client_id}", Fore.BLUE)
        return time_sync_pb2.Empty()

    def StreamTimeUpdates(self, request, context):
        next_update_time = time.time()
        while context.is_active():
            if time.time() >= next_update_time:
                # Define o próximo tempo de atualização
                next_update_time += 20
                current_time = time.time()
                seconds = int(current_time)
                milliseconds = int((current_time - seconds) * 1000)
                yield time_sync_pb2.TimeUpdate(seconds=seconds, milliseconds=milliseconds)
                # Se houver tempo restante, dormir até o próximo tempo de atualização
                sleep_time = next_update_time - time.time()
                if sleep_time > 0:
                    time.sleep(sleep_time)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    time_sync_service = TimeSyncService()
    time_sync_pb2_grpc.add_TimeSyncServiceServicer_to_server(time_sync_service, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    log("🚀 Servidor iniciado. Aguardando clientes...", Fore.GREEN, Style.BRIGHT)
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        log("🛑 Servidor encerrado manualmente.", Fore.RED, Style.BRIGHT)
    finally:
        server.stop(0)

if __name__ == '__main__':
    serve()
