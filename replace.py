#!/usr/bin/python

'''
Write a function replace(s, old, new) that replaces all occurences of old with new in a string s:
test(replace('Mississippi', 'i', 'I'), 'MIssIssIppI')

s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
test(replace(s, 'om', 'am'),
       'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!')

test(replace(s, 'o', 'a'),
       'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!')
'''



# this is the correct way: use split and join to replce all occurences of old 
def replace(s, old, new):
    s = s.split()
    
    if len(s) > 1:
        new_sent = []
        for word in s:
            if old in word:
                new_word = word.split(old)
                new_word = new.join(new_word)
                new_sent.append(new_word)
            else:
                new_sent.append(word)

        new_sent = " ".join(new_sent)
        return new_sent
    
    if len(s) == 1:
        word = s[0]
        new_word = word.split(old)
        new_word = new.join(new_word)
        return new_word




# the following way can only handle single occurence of old in the sentence.  

# def replace(s, old, new):
#     s = s.split()
    
#     if len(s) > 1:
#         new_sent = []
#         for word in s:
#             if old in word:
#                  start = word.index(old[0])
#                  end = start + len(old)
#                  new_word = word[:start]+new+word[end:]
#                  new_sent.append(new_word)
#             else:
#                 new_sent.append(word)

#         new_sent = " ".join(new_sent)
#         return new_sent
    
#     if len(s) == 1:
#         word = s[0]
#         new_word = word.split(old)
#         new_word = new.join(new_word)
#         return new_word        

s = 'I love bonono!  Bonono is my favorite food.  Bonono, bonono, bonono, yum!'
result1 = replace(s, 'ono', 'ana')
print(result1)
result2 = replace("Mississippi", "i", "I")
print(result2)