import sys
import os
import hashlib
import string
import random

onlylower = string.ascii_lowercase
letters = string.ascii_lowercase + string.whitespace

# functions
def generatekey(clear):
    key = ''.join([random.choice(onlylower) for n in range(len(clear))])
    return key

def encryption(clear, key):
    crypted = ''
    for i in range(len(clear)):
        crypted += onlylower[(onlylower.index(key[i]) + onlylower.index(clear[i])) % 26]
    return crypted

def decrypt(crypted, key):
    return clear

#
print(len(onlylower))
inputString = input("Enter a String to encrypt : ")
print("Your message : ", inputString)

key = generatekey(inputString)
print(key)
print(encryption(inputString, key))




#génération du hash
# hashString = hashlib.md5(str.encode(myString))
# print("Et voici son hash : ", hashString.hexdigest())
