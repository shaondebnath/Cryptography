# Cryptography - Python

## Cryptography_ServerClient_Multithread
run serverRSA__multithread.py in server machine

run clientRSA_multithread.py from client machine. (multiple client communication possible)


## Cryptography_ServerClient_singlethread
run serverRSA_singleThread.py in server machine

run clientRSA_singleThread.py from client machine. 

## BasicCryptography
It shows the basic encryption and decryption in both AES and RSA methods

run cryptographyRSA.py

Generate public and private key and save them as file. During encryption or decryption, it uses those files.

## GRPC

This version is created using grpc framework, Please make sure you have grpc requirements installed before using it. for more info visit https://grpc.io/docs/quickstart/python.html

Use Virtualenv: 

sudo apt-get install virtualenv

if you have multiple version of phython in your PC, use phython > 3.5 to create venv

 $ which python3
 
 result is like : /usr/bin/python3
 
 $ virtualenv venvSila -p /usr/bin/python3
 
 $ source venvSila/bin/active
 
 $ cd Cryptography-Python/GRPC/
 
 $ pip install - r requirements.txt


create ssl key:

$ openssl req -newkey rsa:2048 -nodes -keyout server.key -x509 -days 365 -out server.crt

run ssl_server.py in server machine

(server machine should have server.crt and server.key)

run ssl_client.py in client machine

(client machine should  have server.crt)


