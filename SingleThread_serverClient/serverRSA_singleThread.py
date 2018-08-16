#!/usr/bin/env python
import os
import sys

import socket
# pip install pycrypto
from Crypto.PublicKey import RSA
from Crypto import Random
#from Crypto.Cipher import AES

#https://medium.com/@weblab_tech/encrypted-client-server-communication-protection-of-privacy-and-integrity-with-aes-and-rsa-in-c7b180fe614e
#https://github.com/mayankgureja/encryptedChatRSA/blob/master/encryptedChat.py
#http://studyraspberrypi.blogspot.com/2016/01/sending-rsa-encrypted-message-from.html


	
if __name__ == "__main__":

    #Generate private and public keys
    random_generator = Random.new().read
    private_key = RSA.generate(1024, random_generator)
    public_key = private_key.publickey()


    #Declartion
    mysocket = socket.socket()
    host = socket.gethostbyname(socket.getfqdn())
    port = 7777
    encrypt_str = "encrypted_message="

    if host == "127.0.1.1":
        import commands
        host = commands.getoutput("hostname -I")
    print "host = " + host

    #Prevent socket.error: [Errno 98] Address already in use
    mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    mysocket.bind((host, port))

    mysocket.listen(5)

    c, addr = mysocket.accept()

    while True:

        #Wait until data is received.
        data = c.recv(1024)
        data = data.replace("\r\n", '') #remove new line character

        if data == "publicKey Request":
            c.send("public_key=" + public_key.exportKey() + "\n")
            print "Public key sent to client."

        elif encrypt_str in data: #Reveive encrypted message and decrypt it.
            data = data.replace(encrypt_str, '')
            print "Received:\nEncrypted message = "+str(data)
            encrypted = eval(data)
            decrypted = private_key.decrypt(encrypted)
            c.send("Server: OK")
            print "Decrypted message = " + decrypted


        elif data == "Quit": break

    #Server to stop
    c.send("Server stopped\n")
    print "Server stopped"
    c.close()

