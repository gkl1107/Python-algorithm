#!/usr/bin/python3

#given a integer N, generate a string of N number of  "+" and "-", beginning with "+"
# for example: if N =5, then '+-+-+'
# for example: if N = 8, then '+-+-+-+-'


def a_function(N):
	N_to_list = [num for num in range(1, N+1)]
	answer = []
	for i in a_list:
		if i % 2 != 0:
			answer.append('+')
		if i % 2 == 0:
			answer.append('-')

	return ''.join(answer)



print(a_function(8))