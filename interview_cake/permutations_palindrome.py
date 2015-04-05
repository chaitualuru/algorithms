def permut_palindrome(st):
	st_map = {}
	for char in st:
		if char in st_map:
			st_map[char] = not st_map[char]
		else:
			st_map[char] = True

	odd_seen = False

	for k in st_map.itervalues():
		if k:
			if odd_seen:
				return False
			else:
				odd_seen = True

	return True

print permut_palindrome("ivicc")