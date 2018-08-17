'''a recursive function to compute the Fibonacci sequence'''

import time



def recursion_Fibonacci(n):
    
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    else:
        new = [recursion_Fibonacci(n-1)[-1] + recursion_Fibonacci(n-2)[-1]]
   
        fib_seq = recursion_Fibonacci(n-1) + new
        
        return fib_seq

recursion_star_time = time.time()    
recursion_Fibonacci(10)
recursion_used_time = time.time()-recursion_star_time
print("recursion_used time", recursion_used_time)



def for_loop_Fibonacci(n):
	
	final_seq = []

	for i in range(0,n):
		if i == 0 or i == 1:
			final_seq.append(1)
		else:
			new = final_seq[-1] + final_seq[-2]
			final_seq.append(new)
	return final_seq

forloop_star_time = time.time()    
for_loop_Fibonacci(10)
forloop_used_time = time.time()-forloop_star_time
print("forloop used time", forloop_used_time)

