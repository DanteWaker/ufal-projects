import threading
import concurrent.futures
import grpc
import time
import random
import vector_clock_pb2
import vector_clock_pb2_grpc
from vector_clock import VectorClock



# Portas que serão usadas pelos servidores
PORTS = [5001, 5002, 5003, 5004]

# Lista para armazenar os servidores para poder encerrá-los mais tarde
servers = []

class VectorClockService(vector_clock_pb2_grpc.VectorClockServiceServicer):
    def UpdateVectorClock(self, request, context):
        try:
            process_id = None
            for key, value in context.invocation_metadata():
                if key == 'process-id':
                    process_id = value
                    break
            
            if process_id is None:
                raise ValueError("ID do processo não encontrado no metadata")

            process_id = int(process_id)  # Converte o ID do processo para int
            print(f"Iniciando a atualização do relógio vetorial para o processo {process_id}...")

            # Sua lógica aqui, utilizando 'process_id' para acessar 'vector_clocks'
            received_vector = [request.vectorClock[str(i)] for i in range(len(PORTS))]
            vector_clocks[process_id].receive_event(received_vector)

            print(f'Processo {process_id} atualizou seu relógio para {vector_clocks[process_id].vector}')
            return vector_clock_pb2.VectorClockReply()
        except Exception as e:
            print(f"Exceção capturada no serviço UpdateVectorClock: {e}")
            context.abort(grpc.StatusCode.INTERNAL, 'Erro interno')


# Dicionário para armazenar as instâncias de VectorClock
vector_clocks = {}
def serve(process_id, port):
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    vector_clocks[process_id] = VectorClock(process_id, len(PORTS))
    vector_clock_pb2_grpc.add_VectorClockServiceServicer_to_server(VectorClockService(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    servers.append(server)
    print(f'Servidor do processo {process_id} rodando na porta {port}...')
    try:
        while True:
            time.sleep(86400)  # Mantém o servidor rodando
    except KeyboardInterrupt:
        server.stop(0)


def send_message(process_id):
    try:
        # Escolhe um processo alvo aleatoriamente, exceto o próprio processo
        target_process_id = process_id
        while target_process_id == process_id:
            target_process_id = random.choice(range(len(PORTS)))

        with grpc.insecure_channel(f'localhost:{PORTS[target_process_id]}') as channel:
            stub = vector_clock_pb2_grpc.VectorClockServiceStub(channel)
            vector_clock = vector_clocks[process_id].send_event()  # Prepara o vetor para envio
            vector_clock_map = {str(i): v for i, v in enumerate(vector_clock)}
            metadata = [('process-id', str(process_id))]
            stub.UpdateVectorClock(vector_clock_pb2.VectorClockRequest(vectorClock=vector_clock_map), metadata=metadata)
            print(f'Processo {process_id} enviou mensagem para processo {target_process_id} com relógio {vector_clock_map}')
    except grpc.RpcError as e:
        print(f"Erro ao enviar mensagem: {e}")



def start_process(process_id):
    # Inicia o servidor em uma thread separada
    threading.Thread(target=serve, args=(process_id, PORTS[process_id]), daemon=True).start()
    time.sleep(2)  # Dá tempo para o servidor iniciar
        time.sleep(random.randint(1, 4))  # Espera por um tempo aleatório
        send_message(process_id)

if __name__ == '__main__':
    for i in range(len(PORTS)):
        threading.Thread(target=start_process, args=(i,), daemon=True).start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        for server in servers:
            server.stop(0)
