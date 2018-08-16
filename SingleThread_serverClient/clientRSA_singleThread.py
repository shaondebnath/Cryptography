#!/usr/bin/env python
import os
import sys

import socket
# pip install pycrypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import AES

	
class encryption:

    def __init__(self, message):
        server = socket.socket()
        host = "130.149.22.93"
        port = 7777

        server.connect((host, port))

        #Tell server that connection is OK
        server.sendall("publicKey Request")

        #Receive public key string from server
        server_string = server.recv(1024)

        #Remove extra characters
        server_string = server_string.replace("public_key=", '')
        server_string = server_string.replace("\r\n", '')

        print "Public Key received ... "


        #Convert string to key
        server_public_key = RSA.importKey(server_string)

        #Encrypt message and send to server
        #message = "secret message is Shaon Debnath"
        encrypted = server_public_key.encrypt(message, 32)
        server.sendall("encrypted_message="+str(encrypted))
        print "Encrypted Message = " + str(encrypted)

        #Server's response
        server_response = server.recv(1024)
        server_response = server_response.replace("\r\n", '')
        if server_response == "Server: OK":
            print "Server decrypted message successfully"

        #Tell server to finish connection
        server.sendall("Quit")
        print(server.recv(1024)) #Quit server response
        server.close()


if __name__ == "__main__":
    encryption("secret message is Shaon Debnath")