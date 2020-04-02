



#generate a number larger than N and smaller than 10**9, and ended with digit zero

#!/usr/bin/python3


import random

def a_function(N):

	answer = random.randint(N+1, 10**7)
	answer = answer*10

	return answer
	



if __name__ == "__main__":

	print(a_function(55789))