"""Command Learn Algorithm"""

def command_learn(elems):
	state_seq_so_far = [[] for x in range(len(elems))]
	
	for i in range(len(elems)):
		for j in range(i):
			if check_reachability(elems[i], elems[j]):
				if not state_seq_so_far[i]:
					state_seq_so_far[i].append(elems[j])
				else:
					if len(state_seq_so_far[j]) + 1 < len(state_seq_so_far[i]):
						state_seq_so_far[i].append(elems[j])

	return state_seq_so_far

def check_reachability(x, y):
	return ((x % 2 == 0) and (y % 2 == 0)) or ((x % 2 != 0) and (y % 2 != 0))

def main():
	# [1,3,9,8,4,3,2,10]
	print command_learn([5,3,9,8,4,3,2,10])

if __name__ == '__main__':
	main()