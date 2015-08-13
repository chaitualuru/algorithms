"""Sudoku Checker"""

def sudoku_checker(A):
	for i in range(len(A)):
		if not valid_line(A[i]):
			return False

	unzipped_A = list(zip(*A))
	for j in range(len(unzipped_A)):
		if not valid_line(unzipped_A[j]):
			return False

	for k in range(0, len(A), 3):
		for l in range(0, len(A), 3):
			grid = []
			for x in A[k:k+3]:
				for y in x[l:l+3]:
					grid.append(y)
			if not valid_line(grid):
				return False

	return True

def valid_line(line):
	return (len(line) == 9 and sum(line) == sum(set(line)))

def main():
	"""Entry point of the program."""
	# valid
	if sudoku_checker([
		[5,3,0,0,7,0,0,0,0],
		[6,0,0,1,9,5,0,0,0],
		[0,9,8,0,0,0,0,6,0],
		[8,0,0,0,6,0,0,0,3],
		[4,0,0,8,0,3,0,0,1],
		[7,0,0,0,2,0,0,0,6],
		[0,6,0,0,0,0,2,8,0],
		[0,0,0,4,1,9,0,0,5],
		[0,0,0,0,8,0,0,7,9]]):
		print "Valid"
	else:
		print "Not Valid"

if __name__ == '__main__':
	main()
