def jump(n):
	if n == 1: 
		return 1
	elif n == 2:
		return 2
	elif n == 3:
		return 4
	else:

		ways = jump(n-3) + jump(n-2) + jump(n-1)
		return ways


print(jump(4))
