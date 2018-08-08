#!/usr/bin/python

'''
Write a program that allows the user to enter a string. 
It then prints a table of the letters of the alphabet in alphabetical order which occur in the string together with the number of times each letter occurs. 
Case should be ignored. 
'''
sent = raw_input("Please enter a sentence:")
#sent = sent.replace(" ", "")
# get rid of all non-alphabet characters (punctuations and spaces). 
sent_clean = "".join([char for char in sent if char.isalpha()])
sent_clean = sent_clean.lower()

dict = {}
for char in sent_clean:
    if dict.get(char) == None:
        dict[char] = 1
    else:
        dict[char] = dict[char] + 1

keys = dict.keys()
#keys = list(k)
keys.sort()

out_file = open("count_alpha_result.csv", "w")
for k in keys:
    out_file.write(k + "," + str(dict[k]) + "\n")

out_file.close()