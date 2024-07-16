from concurrent import futures
import grpc
import chat_pb2
import chat_pb2_grpc
import threading

def send_messages(stub):
    while True:
        message = input("Digite a sua mensagem: ")
        yield chat_pb2.ChatMessage(sender="SeuNome", message=message)

def receive_messages(stub):
    for message in stub.Chat(chat_pb2.ChatMessage(sender="SeuNome", message="")):
        print(f"Recebido: {message.message} de {message.sender}")

def run():
    channel = grpc.insecure_channel('localhost:3000')
    stub = chat_pb2_grpc.ChatServiceStub(channel)

    response_iterator = stub.Chat(send_messages(stub))
    for response in response_iterator:
        print(f"Recebido: {response.message} de {response.sender}")


if __name__ == '__main__':
    run()
