"""Rotate Array"""

def rotate_array(A, rot_num):
	"""Return rotated array"""
	rev_A = A[::-1]
	return rev_A[0:rot_num][::-1] + rev_A[rot_num:len(rev_A)][::-1]

def main():
	"""Entry point of the program."""
	# [3,4,5,6,1,2]
	print rotate_array([1,2,3,4,5,6], 4)

if __name__ == '__main__':
	main()
