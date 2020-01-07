import sys
import os
import hashlib
import string
import random

# functions
def generatekey(clear):
    key = ''.join([chr(random.randint(32,126)) for n in range(len(clear))])
    return key

def encrypt(clear, key):
    crypted = ''
    for i in range(len(clear)):
        crypted += chr((ord(clear[i])+ord(key[i]))%127)
    return crypted

def decrypt(crypted, key):
    clear = ''
    for i in range(len(crypted)):
        clear += chr((ord(crypted[i])-ord(key[i]))%127)
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
