import sys
import os
import hashlib
import string
import random

# functions
def generatekey(clear):
    key = ''.join([chr(random.randint(0,255)) for n in range(len(clear))])
    return key

def encrypt(clear, key):
    crypted = ''
    for i in range(len(clear)):
        crypted += chr((ord(clear[i])+ord(key[i])%256))
    return crypted

def decrypt(crypted, key):
    clear = ''
    for i in range(len(crypted)):
        clear += chr((ord(crypted[i])-ord(key[i])%256))
    return clear

######
inputString = input("Enter a String to encrypt : ")
print("Your message :", inputString)

key = generatekey(inputString)
print(key)
encrypted = encrypt(inputString, key)
print(encrypted)
decrypted = decrypt(encrypted, key)
print(decrypted)





#génération du hash
# hashString = hashlib.md5(str.encode(myString))
# print("Et voici son hash : ", hashString.hexdigest())