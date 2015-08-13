"""Phone Number Pneumonic"""

def get_all_combos(M, seq, len_so_far, str_a):
	if len_so_far == len(seq):
		print ''.join(str_a)
	else:
		for c in M[int(seq[len_so_far])]:
			str_a[len_so_far] = c
			get_all_combos(M, seq, len_so_far + 1, str_a)


def main():
	"""Entry point of the program."""
	combination = '35791'
	str_a = [0] * len(combination)
	get_all_combos(['0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'], combination, 0, str_a)

if __name__ == '__main__':
	main()