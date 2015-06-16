"""Merge Meetings"""

def merge_meetings(meetings):
	"""Returns merged meeting times."""
	if not meetings:
		return None
	sorted_meetings = sorted(meetings)
	start = sorted_meetings[0][0]
	end = sorted_meetings[0][1]
	result = list()
	for meeting in sorted_meetings[1:]:
		if end >= meeting[0]:
			end = max(end, meeting[1])
		else:
			result.append((start, end))
			start = meeting[0]
			end = meeting[1]
	result.append((start, end))
	return result

def main():
	"""Entry point for the program."""	
	# None
	print merge_meetings([])
	# [(1, 3)]
	print merge_meetings([(1, 3)])
	# [(1, 5)]
	print merge_meetings([(1, 3), (2, 5)])
	# [(1, 8), (9, 13)]
	print merge_meetings([(1, 4), (10, 12), (2, 7), (6, 8), (9, 13)])
	# [(1, 10)]
	print merge_meetings([(1, 10), (2, 6), (3, 5), (7,9)])
	
if __name__ == '__main__':
	main()
