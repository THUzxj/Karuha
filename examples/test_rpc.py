import grpc

from tinode_grpc import pb
import tinode_grpc

def run():
    with grpc.insecure_channel('localhost:40051') as channel:
        stub = tinode_grpc.pbx.PluginStub(channel)
        response = stub.Account(pb.AccountEvent())
        print("Greeter client received: " + str(response))

run()
