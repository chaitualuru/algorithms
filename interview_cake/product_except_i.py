"""Product Except i"""
"""Without division."""
"""Two passes. Go forwards storing all products before i at i. Go backwards storing all products after i at i."""
"""With division"""
"""Calculate product of all members and then divide each member as you go"""

def get_product_except_i(nums):
	"""Return an array of products of nums except the num at its own index."""
	if not nums:
		return None
	if len(nums) == 1:
		return [0]
	products = [1] * len(nums)
	product_so_far = 1
	for i in range(len(nums)):
		products[i] *= product_so_far
		product_so_far *= nums[i]
	index = len(nums) - 1
	product_so_far = 1
	while index >= 0:
		products[index] *= product_so_far
		product_so_far *= nums[index]
		index -= 1
	return products
	

def main():
	"""Entry point of the program."""
	# 0
	print get_product_except_i([1])
	# None
	print get_product_except_i([])
	# [2, 10]
	print get_product_except_i([10, 2])
	# [12, 15, 20]
	print get_product_except_i([5, 4, 3])

if __name__ == '__main__':
	main()
