#!/usr/bin/env python
import os
import sys

# pip install pycrypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import AES

#https://medium.com/@weblab_tech/encrypted-client-server-communication-protection-of-privacy-and-integrity-with-aes-and-rsa-in-c7b180fe614e
#https://github.com/mayankgureja/encryptedChatRSA/blob/master/encryptedChat.py
#http://studyraspberrypi.blogspot.com/2016/01/sending-rsa-encrypted-message-from.html
#random_generator = Random.new().read
#private_key = RSA.generate(1024, random_generator)
#public_key = private_key.publickey()
#print ("public_key = "+ str(public_key.exportKey()))

public_keyStr = ""
private_keyStr = ""

class Crypto():
    def generateKey(self):
        if os.path.exists('privatekey'):
            print 'Private Key found.'
            '''with open('privatekey', 'rb') as privatefile:
                private_keyStr = privatefile.read()
                #privkey = rsa.PrivateKey.load_pkcs1(keydata,'PEM')
                print "Exit- " +private_keyStr

            with open('publickey.pem', 'rb') as publicfile:
                public_keyStr = publicfile.read()
                #privkey = rsa.PrivateKey.load_pkcs1(keydata,'PEM')
                print "Exit- " +public_keyStr'''

        else:
            random_generator = Random.new().read
            private_key = RSA.generate(1024, random_generator)
            public_key = private_key.publickey()

            private_keyStr = str(private_key.exportKey())
            public_keyStr = str(public_key.exportKey())

            with open ("privatekey", "w") as privatefile:
                privatefile.write(private_keyStr)
                privatefile.close

            with open ("publickey.pem", "w") as publicfile:
                publicfile.write(public_keyStr)
                publicfile.close

        #print ("public_key = "+ public_keyStr)

    def encrypt(self, message):
        if os.path.exists('publickey.pem'):
            with open ("publickey.pem", 'rb') as publicfile:
                public_keyStr = publicfile.read()

            public_key = RSA.importKey(public_keyStr)

            encryptedMsg = public_key.encrypt(message, 32)
            #print("encrypted_message="+str(encryptedMsg))
            return encryptedMsg

        else:
            print ("publickey.pem does not exists. Generate RSA KEY")

     	
    def decrypt(self, message):
        if os.path.exists('privatekey'):
            with open ("privatekey", 'rb') as publicfile:
                private_keyStr = publicfile.read()

            private_key = RSA.importKey(private_keyStr)
            decryptedMsg = private_key.decrypt(message)
            return decryptedMsg

        else:
            print ("privatekey does not exists. Generate RSA KEY")


        
	
if __name__ == "__main__":
    Crypto().generateKey()

    message = "Here is my Secret Message"

    myMsg = Crypto().encrypt(message)
    print("encrypted_message="+str(myMsg))
	
    decrMsg = Crypto().decrypt(myMsg)
    print("decrypted_message="+str(decrMsg))
