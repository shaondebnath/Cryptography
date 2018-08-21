# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc

import helloworld_pb2
import helloworld_pb2_grpc


'''def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:    
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
    print("Greeter client received: " + response.message)'''

#host = '130.149.22.93'
host = 'localhost'
port = '50051'

def run():
    #channel = grpc.insecure_channel('localhost:50051')
    channel = grpc.insecure_channel('{}:{}'.format(host, port))
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    try:
      response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
      print("Greeter client received: " + response.message)
    except grpc.RpcError as err:
      print('Type:', type(err))
      print('Attributes:', dir(err))
    #print("Greeter client received: " + response.message)

def runSecured():

    with open('server.crt', 'rb') as f:
        trusted_certs = f.read()

    credentials = grpc.ssl_channel_credentials(open('server.crt', 'rb').read()) #grpc.ssl_channel_credentials(root_certificates=trusted_certs)
    channel = grpc.secure_channel('{}:{}'.format(host, port), credentials)


    stub = helloworld_pb2_grpc.GreeterStub(channel)
    try:
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
        print("secured client received: " + response.message)
    except grpc.RpcError as err:
        print('Type:', type(err))
        print('Attributes:', dir(err))
    #print("secured client received: " + response.message)


if __name__ == '__main__':
    #run()
    runSecured()

