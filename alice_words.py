'''
Write a program that creates a text file named alice_words.txt containing an alphabetical listing of all the words, and the number of times each occurs.
'''

word_dict = {}

with open("alice_in_wonderland.txt") as file:
	line = file.readline()
	while line:
		no_punct = "".join([char for char in line if char.isalpha() or char.isspace() or char == '-' or char == "'"])
		no_doubleHyphen = no_punct.replace("--", " ")
		no_astro = no_doubleHyphen.replace("'s", " ")
		clean_line = no_astro.lower()
		
		words = clean_line.split()
		
		for word in words:
			if word_dict.get(word) == None:
				word_dict[word] = 1
			else:
				word_dict[word] = word_dict[word] + 1

		line = file.readline()


# write the wordlist result into a new file called "alice_words.txt"
sorted_words = sorted(word_dict.keys())

outfile = open("alice_words.txt","w")

for word in sorted_words:
	outfile.write(word + "," + str(word_dict[word]) + "\n")


# find the longest word in the wordlist
word_length = {}
for word in word_dict.keys():
	word_length[word] = len(word)

max_length = max(v for v in word_length.values())
for k,v in word_length.items():
	if v == max_length:
		print("longest word is: ", k, v)



