#!/usr/bin/env python
import os
import sys

import socket
from threading import Thread 
from SocketServer import ThreadingMixIn 

# pip install pycrypto
from Crypto.PublicKey import RSA
from Crypto import Random
#from Crypto.Cipher import AES

#https://medium.com/@weblab_tech/encrypted-client-server-communication-protection-of-privacy-and-integrity-with-aes-and-rsa-in-c7b180fe614e
#https://github.com/mayankgureja/encryptedChatRSA/blob/master/encryptedChat.py
#http://studyraspberrypi.blogspot.com/2016/01/sending-rsa-encrypted-message-from.html

TCP_IP = '0.0.0.0' 
TCP_PORT = 2004 
BUFFER_SIZE = 1024



class ClientThread(Thread): 
 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print "[+] New server socket thread started for " + ip + ":" + str(port) 
 
    def run(self): 
       
        while True : 
            #Wait until data is received.
            data = conn.recv(BUFFER_SIZE)
            data = data.replace("\r\n", '') #remove new line character

            if data == "publicKey Request":
                conn.send("public_key=" + public_key.exportKey() + "\n")
                print "Public key sent to client."

            elif encrypt_str in data: #Reveive encrypted message and decrypt it.
                data = data.replace(encrypt_str, '')
                print "Received:\nEncrypted message = "+str(data)
                encrypted = eval(data)
                decrypted = private_key.decrypt(encrypted)
                conn.send("Server: OK")
                print "Decrypted message = " + decrypted


            elif data == "Quit": 
                #Server to stop
                conn.send("Connection Quit\n")
                print "Connection Quit"
                conn.close()

                break


	
#if __name__ == "__main__":

    # Multithreaded Python server : TCP Server Socket Program Stub

#Generate private and public keys
random_generator = Random.new().read
private_key = RSA.generate(1024, random_generator)
public_key = private_key.publickey()


#server


tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostbyname(socket.getfqdn())
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((host, TCP_PORT)) 
threads = [] 

encrypt_str = "encrypted_message="

if host == "127.0.1.1":
    import commands
    host = commands.getoutput("hostname -I")
print "host = " + host
 
while True: 
    tcpServer.listen(4) 
    print ("Multithreaded Python server : Waiting for connections from TCP clients...") 
    (conn, (ip,port)) = tcpServer.accept() 
    newthread = ClientThread(ip,port) 
    newthread.start() 
    threads.append(newthread) 

    for t in threads: 
        t.join() 





#Declartion
#mysocket = socket.socket()
host = socket.gethostbyname(socket.getfqdn())
#port = 7777
encrypt_str = "encrypted_message="

if host == "127.0.1.1":
    import commands
    host = commands.getoutput("hostname -I")
print ("host = " + host)










