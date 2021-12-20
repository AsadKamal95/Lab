# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 14:39:39 2021

@author: SELAB
"""

def encrypt(text,key):
    char=[]
    lis=[]
    for x in range(len(text)):
        char.append(ord(text[x]))
        char[x]=char[x]+key
        if(char[x]>90 and char[x]<97):
            char[x]=65
        if(char[x]>122):
            char[x]=97
        lis.append(chr(char[x]))
    x=''.join(lis)    
    print(x)
    return

def decypt(text,key):
    char=[]
    lis=[]
    for x in range(len(text)):
        char.append(ord(text[x]))
        char[x]=char[x]-key
        if(char[x]<65 and char[x]<97):
            char[x]=84
        lis.append(chr(char[x]))
    x=''.join(lis)    
    print(x)
    return


decypt("KLMLUKAOLMVYA", 7)
#decypt("klmlukaolmvya", 7)
print('\n')
#encrypt("defendthefort",7)
encrypt("DEFENDTHEFORT",7)

print(" My codeeee")
