'''
Write a function that takes a string as a parameter and returns True if the string is a palindrome, False otherwise. 
Remember that a string is a palindrome if it is spelled the same both forward and backward. 
for example: radar is a palindrome. 
for bonus points palindromes can also be phrases, but you need to remove the spaces and punctuation before checking. 
for example: madam i’m adam is a palindrome. Other fun palindromes include:

kayak
aibohphobia
Live not on evil
Reviled did I live, said I, as evil I did deliver
Go hang a salami; I’m a lasagna hog.
Able was I ere I saw Elba
Kanakanak – a town in Alaska
Wassamassaw – a town in South Dakota
'''



def removeWhite(s):
    s = "".join(char.lower() for char in s if char.isalpha())
    return s

def isPal(s):
    if len(s) <= 1:
        return True
    else:
        if s[0] == s[-1]:
            left = s[1:len(s)-1]
            #print(left)
            if isPal(left):
                return True
        else:
            return False
    
print(isPal(removeWhite("aibohphobia")))
print(isPal(removeWhite("go hang a salami; i’m a lasagna hog.")))