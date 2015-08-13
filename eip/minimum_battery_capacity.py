"""Minimum Battery Capacity"""

def get_min_capacity(coords):
	min_val = coords[0][1]
	max_so_far = coords[1][1] - coords[0][1]
	for coord in coords:
		min_val = min(min_val, coord[1])
		max_so_far = max(max_so_far, coord[1] - min_val)

	return max_so_far

def main():
	print get_min_capacity([(0,9,0), (0,3,0), (0,4,0), (0,1,0), (0,5,0)])

if __name__ == '__main__':
	main()
