'''
a function called rot13 that uses the Caesar cipher to encrypt a message. 
The Caesar cipher works like a substitution cipher but each character is replaced by the character 13 characters to ‘its right’ in the alphabet. 
So for example the letter a becomes the letter n. 
If a letter is past the middle of the alphabet then the counting wraps around to the letter a again, so n becomes a, o becomes b and so on.
'''

import string 
def rot13(mess):
    caesar_cipher = string.ascii_lowercase[13:] + string.ascii_lowercase[0:13]
    upper_caesar = caesar_cipher.upper()
    encrypt = []
    for c in mess:
        if c in string.ascii_uppercase:
            sub = upper_caesar[string.ascii_uppercase.index(c)]
            encrypt.append(sub)
        elif c in string.ascii_lowercase:
            sub = caesar_cipher[string.ascii_lowercase.index(c)]
            encrypt.append(sub)
        else:
            encrypt.append(c)
    result = "".join(encrypt)
    return result
    

print(rot13('abcde'))
print(rot13('nopqr'))
print(rot13(rot13('Since rot13 is symmetric you should see this message')))

