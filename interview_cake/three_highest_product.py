"""Highest Product of 3"""

def highest_3(nums):
	"""Return the highest possible product of 3 numbers in nums."""
	if len(nums) < 3 or not nums:
		return None
	highest = nums[0]
	lowest = nums[0]
	highest_2 = highest
	lowest_2 = lowest
	highest_3 = highest
	for num in nums[1:]:
		highest_3 = max(highest_3, highest_2 * num, lowest_2 * num)
		highest_2 = max(highest_2, highest * num, lowest * num)
		lowest_2 = min(lowest_2, lowest * num, highest * num)
		highest = max(highest, num)
		lowest = min(lowest, num)
	return highest_3

def main():
	"""Entry point for the program."""
	# None
	print highest_3([])
	# None
	print highest_3([2])
	# None
	print highest_3([2, 3])
	# 6
	print highest_3([1, 2, 3])
	# 900
	print highest_3([-10, 2, -10, 5, 7, 9])
	# 1800
	print highest_3([-15, -5, 12, 10, -10, 6])
	  
if __name__ == '__main__':
	main()
	  