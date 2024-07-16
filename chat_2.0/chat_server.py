from concurrent import futures
import grpc
import chat_pb2_grpc

class ChatService(chat_pb2_grpc.ChatServiceServicer):
    def Chat(self, request_iterator, context):
        for message in request_iterator:
            print(f"Recebendo mensagem de {message.sender}: {message.message}")
            yield message


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatService(), server)
    server.add_insecure_port('[::]:3000')
    
    server.start()
    
    print("Server iniciado. Verificando as mensagens...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
