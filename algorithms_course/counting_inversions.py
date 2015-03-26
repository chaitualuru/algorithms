def count_inversions(list):
	if len(list) == 1:
		return 0
	else:
		mid_idx = len(list) // 2
		left_count = count_inversions(list[:mid_idx])
		right_count = count_inversions(list[mid_idx:])
		