#!/usr/bin/python

def longestCommonPrefix(strs):

	if len(strs) == 0:
		return 'does not work: empty list'

	shortest_word = min(strs, key = len)
	#print(shortest_word)

				
	for slice_range in range(len(shortest_word), 0, -1):
		    partials = []
		    for word in strs:
		        partials.append(word[0:slice_range])

		    test = allMatch(partials)
		    if test == True:
		    	return partials[0]
		    else:
		    	continue

	return 'does not exsit'


# def allMatch(wordList, aWord):
# 	result = True
# 	for i in range(0, len(wordList)):
# 		if wordList[i] == aWord:
# 			pass
# 		else: 
# 			result = False
# 			break
# 	return result		


def allMatch(wordList):

	if len(set(wordList)) == 1:
		return True
	else:
		return False


if __name__ == '__main__':
	#print(longestCommonPrefix(['flower','flight','flow']))
	# print(longestCommonPrefix(['flower','flowing','flow']))
	# print(longestCommonPrefix(['flower','fat','flow']))
	# print(longestCommonPrefix(['flower','alight','flow']))
	print(longestCommonPrefix(['dog','car','racecar']))
	# print(longestCommonPrefix(['dog']))
	#print(longestCommonPrefix([]))



