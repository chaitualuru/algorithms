def merge_meetings(meetings):
	result = []
	meeting_sort = sorted(meetings)
	prev_start = meeting_sort[0][0]
	prev_end = meeting_sort[0][1]
	for m in meeting_sort[1:]:
		if m[0] > prev_end:
			result.append((prev_start, prev_end))
			prev_end = m[1]
			prev_start = m[0]
		else:
			prev_end = m[1]
	result.append((prev_start,prev_end))
	return result

print merge_meetings([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])