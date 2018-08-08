'''
Write a program that asks the user for a sentence in English and then translates that sentence to Pirate.

'''

# read in the file of english-to-pirate words and create a dict
import string

e_to_p = {}
with open("englishToPirate.txt") as transTable:
	line = transTable.readline()
	while line:
		words = line.split()
		e_to_p[words[0]] = words[1]
		line = transTable.readline()
del e_to_p["English"]


# sent = input("Please enter a sentence:")
sent = '''my professor is your man, good list! the student said: "hotel? " '''

# inserting a space before and after every punctuation 
# clean_sent = ""
# for letter in sent:
#     if letter in string.punctuation:
#         clean_sent = clean_sent + " " + letter + " "
#     else:
#     	clean_sent = clean_sent + letter

# # translate every e word into p word
# result = []

# for word in clean_sent.split():
# 	if word in e_to_p:
# 		result.append(e_to_p[word])
# 	else:
# 		result.append(word)

# p_sent = " ".join(result)


# # give correct spaces before and after the punctuations.  
# import re
# p_sent = re.sub(r'\s([,.?!:])',r'\1',p_sent)
# p_sent = re.sub(r'(["])\s',r'\1',p_sent)

# print(p_sent)


'''
---------below is another way to do the translation----------------------
'''

import re 
p_sent = sent

# sub: substitution 
# \b: mark the bountry, boundry is anything except alphabets and numbers
# %s: place holder of the variable
# %: what ever after the % is the variable 
for k,v in e_to_p.items():
	p_sent = re.sub(r'\b%s\b' % k, v, p_sent)

print(p_sent)




