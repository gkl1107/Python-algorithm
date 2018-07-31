import random
from random import randint
import numpy

def cut_rope(N,T):

	rope = [x for x in range(N+1)]
	#print(rope)
	select_int_pool = [x for x in range(1,N)]
	#print(select_int_pool)

	for time in range(1,T+1):
		#print("the", time, "time")

		if len(select_int_pool) >= 2:	

			select_int_1 = random.choice(select_int_pool)
			#print(select_int_1)
			select_int_pool.remove(select_int_1)

			select_int_2 = random.choice(select_int_pool)
			#print(select_int_2)
			select_int_pool.remove(select_int_2)

			if select_int_1 < select_int_2:
				resulting_rope_1 = rope[:rope.index(select_int_1)]
				resulting_rope_2 = rope[rope.index(select_int_1):rope.index(select_int_2)]
				resulting_rope_3 = rope[rope.index(select_int_2):]
			if select_int_2 < select_int_1:
				resulting_rope_1 = rope[:rope.index(select_int_2)]
				resulting_rope_2 = rope[rope.index(select_int_2):rope.index(select_int_1)]
				resulting_rope_3 = rope[rope.index(select_int_1):]

			max_rope_len = max([len(r) for r in [resulting_rope_1,resulting_rope_2, resulting_rope_3]])
			#print(max_rope_len)
			longest_rope = [r for r in [resulting_rope_1,resulting_rope_2, resulting_rope_3] if len(r) == max_rope_len][0]
			rope = longest_rope
			select_int_pool = [x for x in rope[1:-1]]
			#print("new rope", rope)
			#print("new pool", select_int_pool)

	return rope


sumlist = []
for i in range(1000):
	S = len(cut_rope(64,5))
	sumlist.append(S)

print(len(sumlist))

mean_of_S = sum(sumlist)/1000
std_of_S = numpy.std(sumlist)

print(mean_of_S)
print(std_of_S)

greater_than_eight = []
for s in sumlist:
	if s > 8:
		greater_than_eight.append(s)

prob_of_eight = float(len(greater_than_eight))/float(len(sumlist))

print(prob_of_eight)

greater_than_four = []
for s in sumlist:
	if s > 4:
		greater_than_four.append(s)

prob_of_four = float(len(greater_than_four))/float(len(sumlist))

print(prob_of_four)
conditional_prob = prob_of_eight / prob_of_four

print(conditional_prob)


