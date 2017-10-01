#!/usr/bin/python

s = b'x' #Insert Hexahexacontadecimal string for 'x'

BASE66_ALPHABET = b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_.~"
BASE = len(BASE66_ALPHABET)

n = 0

for c in s:
    n = n * BASE + BASE66_ALPHABET.index(c)

print(n) #Prints number decoded from Hexahexacontadecimal
