'''
iterate from the end of the string to front, but this will change the word order, which led to backward sentence

'''

# def seg(s, wordDict):
	
# 	segments = []
# 	left = s
# 	while len(left) > 0:
# 		for index in range(len(left)-1, -1, -1):
# 			target = left[index:]
# 			if target in wordDict:
# 				left = s[0:index]
# 				segments.append(target)
# 				#print(segments)

# 	return " ".join(segments)



# r = seg("catsanddog", ["cat","cats","and","sand","dog"])
# print(r)




'''
iterate from the front of the string to the end

'''

def seg(s, wordDict):
	
	segments = []
	copy = s
	while len(copy) > 0:
		for index in range(0, len(copy)):
			target = copy[0:index]
			if target in wordDict:
				copy = copy[index:]
				segments.append(target)
				#print(segments)

	sents = [" ".join(segments)]

	segments = []
	while len(s) > 0:
		for index in range(len(s),-1,-1):
			target = s[0:index]
			if target in wordDict:
				s = s[index:]
				segments.append(target)
				#print(segments)
	sents.append(" ".join(segments))

	return sents



possible_sents = seg("catsanddog", ["cat","cats","and","sand","dog"])
print(possible_sents)