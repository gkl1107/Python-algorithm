#!/usr/bin/python
def increment(num):

	num_str = str(num)
	result = ''

	for n in num_str:
		n = str(int(n) + 1)
		result = result + n
	return int(result)



if __name__ == '__main__':
	print increment(6666)
	print increment(9730)