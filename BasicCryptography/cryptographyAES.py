#!/usr/bin/env python
import os
import sys

# pip install pycrypto
from Crypto.Cipher import AES

#https://medium.com/@weblab_tech/encrypted-client-server-communication-protection-of-privacy-and-integrity-with-aes-and-rsa-in-c7b180fe614e
#https://github.com/mayankgureja/encryptedChatRSA/blob/master/encryptedChat.py
#http://studyraspberrypi.blogspot.com/2016/01/sending-rsa-encrypted-message-from.html

#key and ivNo should be same to encrypt and decrypt
key = 'siLaEncryptKey01'   #write 16 degit key
ivNo = 'siLaEncryptIV001'  #write 16 degit IV
	

class Encryption:
    def __init__(self, message):
        obj = AES.new(key, AES.MODE_CBC, ivNo)
        #message = "The answer is no"		
        ciphertext = obj.encrypt(message)
        print ("msg= " +ciphertext)
        return ciphertext
   
if __name__ == "__main__":

    #abc = Encryption('Shaon')
    obj = AES.new(key, AES.MODE_CBC, ivNo)
    message = "shaon"
    ciphertext = obj.encrypt(message)
    print ("msg= " +ciphertext)
	
    obj2 = AES.new(key, AES.MODE_CBC, ivNo)	
    orgMsg=obj2.decrypt(ciphertext)
    print ("msg= " +orgMsg)
   

