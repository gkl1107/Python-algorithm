
# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].



def findMissing(A):
	s = {x for x in A if x > 0}
	if not s:
		return 1
	last = max(s)+1

    # Find elements present in either of the two sets, but not common to both the sets
	new_set = s^set(range(1, last))

	if not new_set:
		return last
	return min(new_set)





if __name__ == "__main__": 


	A = [1, 3, 6, 4, 1, 2]
	# A = [1,2,3]
	# A = [-1, -3]
	# A = [-999999,5,9]
	# A = [0,23,56,79,104,199]
	print(findMissing(A))