"""Dutch National Flag Partiitoning Algorithm"""

# Bottom -> [0 : smaller - 1]
# Equal -> [smaller : equal - 1]
# Unclassified -> [equal : larger - 1]
# Top -> [larger : len(A) - 1]

def dutch_partition(A, i):
	"""Return array with elements less than A[i] followed by elements equal to A[i]
		followed by elements greater than A[i]."""
	pivot = A[i]
	smaller = 0
	equal = 0
	larger = len(A) - 1
	while equal <= larger:
		if A[equal] < pivot:
			A[smaller], A[equal] = A[equal], A[smaller]
			smaller += 1
			equal += 1
		elif A[equal] == pivot:
			equal += 1
		else:
			A[equal], A[larger] = A[larger], A[equal]
			larger -= 1
	return A


def main():
	"""Entry point for the program."""
	# [1]
	print dutch_partition([1], 0)
	# [2, 2, 2, 2]
	print dutch_partition([2, 2, 2, 2], 1)
	# [10, 10, 23, 12, 25, 30]
	print dutch_partition([10, 23, 12, 10, 25, 30], 0)
	# [3, 4, 7, 10, 12]
	print dutch_partition([10, 12, 3, 4, 7], 4)

if __name__ == '__main__':
	main()
