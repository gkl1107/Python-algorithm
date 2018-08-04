#!/usr/bin/python

'''
A function that implements a substitution cipher.
the function takea two parameters, the message you want to encrypt, 
and a string that represents the mapping of the 26 letters in the alphabet. 
'''

import string

def cipher(message, str_mapping):
    upperCase_mapping = str_mapping.upper()
    encrypt = []
    for c in message:
        if c in string.ascii_uppercase:
            sub = str_mapping.upper()[string.ascii_uppercase.index(c)]
            encrypt.append(sub)
        elif c in string.ascii_lowercase:
            sub = str_mapping[string.ascii_lowercase.index(c)]
            encrypt.append(sub)
        else:
            encrypt.append(c)
    result = "".join(encrypt)
    return result
    
            
    
    
r = cipher("Write a function that implements a substitution cipher.","efghijklmnopqrstuvwxyzabcd")
print(r)    