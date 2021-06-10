# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 13:41:00 2021

@author: user
"""
from random import randint
############### OTP

def returnAscii(arg):
    if (arg=='A'):
        return '00000'
    if (arg=='B'):
        return '00001'
    if (arg=='C'):
        return '00010'
    if (arg=='D'):
        return '00011'
    if (arg=='E'):
        return '00100'
    if (arg=='F'):
        return '00101'
    if (arg=='G'):
        return '00110'
    if (arg=='H'):
        return '00111'
    if (arg=='I'):
        return '01000'
    if (arg=='J'):
        return '01001'
    if (arg=='K'):
        return '01010'
    if (arg=='L'):
        return '01011'
    if (arg=='M'):
        return '01100'
    if (arg=='N'):
        return '01101'
    if (arg=='O'):
        return '01110'
    if (arg=='P'):
        return '01111'
    if (arg=='Q'):
        return '10000'
    if (arg=='R'):
        return '10001'
    if (arg=='S'):
        return '10010'
    if (arg=='T'):
        return '10011'
    if (arg=='U'):
        return '10100'
    if (arg=='V'):
        return '10101'
    if (arg=='W'):
        return '10110'
    if (arg=='X'):
        return '10111'
    if (arg=='Y'):
        return '11000'
    if (arg=='Z'):
        return '11001'
    if (arg=='.'):
        return '11010'
    if (arg=='!'):
        return '11011'
    if (arg=='?'):
        return '11100'
    if (arg=='(' ):
        return '11101'
    if (arg== ')' ):
        return '11110'
    if (arg=='-'):
        return '11111'
    
def returnLatin(arg):
    if (arg=='00000'):
        return 'A'
    if (arg=='00001'):
        return'B'
    if (arg=='00010'):
        return 'C'
    if (arg=='00011'):
        return 'D'
    if (arg=='00100'):
        return 'E'
    if (arg=='00101'):
        return  'F'
    if (arg=='00110'):
        return 'G'
    if (arg=='00111'):
        return 'H'
    if (arg=='01000'):
        return 'I'
    if (arg=='01001'):
        return  'J'
    if (arg=='01010'):
        return 'K'
    if (arg== '01011'):
        return 'L'
    if (arg=='01100'):
        return 'M'
    if (arg== '01101'):
        return 'N'
    if (arg=='01110'):
        return  'O'
    if (arg== '01111'):
        return 'P'
    if (arg== '10000'):
        return 'Q'
    if (arg== '10001'):
        return 'R'
    if (arg=='10010'):
        return  'S'
    if (arg== '10011'):
        return 'T'
    if (arg=='10100'):
        return 'U' 
    if (arg== '10101'):
        return 'V'
    if (arg== '10110'):
        return 'W'
    if (arg== '10111'):
        return 'X'
    if (arg== '11000'):
        return 'Y'
    if (arg== '11001'):
        return 'Z'
    if (arg== '11010'):
        return '.'
    if (arg== '11011'):
        return '!'
    if (arg== '11100'):
        return '?'
    if (arg==  '11101'):
        return '('
    if (arg==  '11110'):
        return ')'
    if (arg=='11111'):
        return '-'
    
    
text= input ("Write the text that you want encrypted: ")
print("You entered",text)
text1=[]
for i in text:
    k=returnAscii(i)
    text1.append(k)
str1=''
k=list(str1.join(text1))
print("Text in bits")
print(k)

keystream=list([randint(0,1) for i in range(5*len(text1))])



 # encryption
cipher=[]
for i in range(len(k)):
    l=int(k[i])^int(keystream[i])
    cipher.append(l)
print("Encrypted in bits: ")
print(cipher)


# decryprion

original=[]
for i in range(len(k)):
    l=int(cipher[i])^int(keystream[i])
    original.append(l)
print("Decrypted in bits: ")
print(original)

given=''
for i in range(int(len(original)/5)):
    s=''
    for j in range(5):
        s+=str(original[(i*5)+j])
    given=given+returnLatin(s)
print(given)        


