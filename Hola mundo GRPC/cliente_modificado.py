import grpc
import helloworld_pb2
import helloworld_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    nombre_usuario = input("Ingresa tu nombre: ")
    response = stub.SayHello(helloworld_pb2.HelloRequest(name=nombre_usuario))
    print("Cliente recibió:", response.message)

if _name_ == '_main_':
    run()