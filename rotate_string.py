#!/usr/bin/python


#Given a string and an offset, rotate the string by offset in place. (rotate from left to right).

def RotateString(inputStr, offset):
	charList = []
	for char in inputStr:
		charList.append(char)
	
	length = len(charList)
	NewStartIndex = length - (offset % length)
	rotatedList = []

	for i in range(NewStartIndex, length):
		rotatedList.append(charList[i])

	for i in range(0, NewStartIndex):
		rotatedList.append(charList[i])

	rotated_string = ''.join(rotatedList)
	return rotated_string



if __name__ == '__main__':
	
	print RotateString("abcdefg", 2)
	print RotateString("abcdefg", 10)

