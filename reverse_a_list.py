'''Write a recursive function to reverse a list.'''

def reverseList(lst):
	if len(lst) == 0:
		return None
	elif len(lst) == 1:
		return lst
	else: 
		return [lst[-1]] + reverseList(lst[0:-1])


def test(inp, expect):
	result = reverseList(inp)
	print(result == expect, "input {}, expect {}, result {}".format(inp, expect, result))

test([1,2,3,4],[4,3,2,1])
test([],None)

