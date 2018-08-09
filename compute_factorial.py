def fact(n):
	try:
		if n == 1:
			return 1
		elif n <= 0:
			raise ValueError("ERROR: please enter positive value.")
		else:
			return n * fact(n-1)
	except ValueError as err:
		return err
		


print(fact(-3))