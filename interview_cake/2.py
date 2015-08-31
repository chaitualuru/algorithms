import unittest

def product_others(A):
	if len(A) < 2:
		return "There are no other elements in the array."
	product = 1
	result = list([])
	result.append(product)
	for i in range(len(A) - 1):
		product *= A[i]
		result.append(product)
	product = 1
	for i in range(len(A) - 1, 0, -1):
		product *= A[i]
		result[i - 1] *= product
	return result 

class ProductOthersTester(unittest.TestCase):
	TEST_DATA = [
		([0], "There are no other elements in the array."),
		([2, 1, 3, 7], [21, 42, 14, 6]),
		([9, 10], [10, 9]),
		([0, 5, 7, 8], [280, 0, 0, 0])]

	def test(self):
		for inp, expected in self.TEST_DATA:
			res = product_others(inp)
			self.assertEqual(res, expected)

if __name__ == '__main__':
	unittest.main()
