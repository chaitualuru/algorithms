import unittest

def highest_three(A):
	if len(A) < 3:
		return "Input needs to contain at least three elements."

	max_three = A[0] * A[1] * A[2]
	max_two = max(A[0] * A[1], A[0] * A[2], A[1] * A[2])
	min_two = min(A[0] * A[1], A[0] * A[2], A[1] * A[2])
	max_one = max(A[0], A[1], A[2])
	min_one = min(A[0], A[1], A[2])

	for num in A[3:]:
		max_three = max(max_two * num, min_two * num, max_three)
		max_two = max(max_one * num, max_two)
		min_two = min(min_one * num, min_two)
		max_one = max(num, max_one)
		min_one = min(num, min_one)

	return max_three

class HighestThreeTester(unittest.TestCase):
	TEST_DATA = [
		([-2, 1, -3, 4], 24),
		([], "Input needs to contain at least three elements.")]

	def test(self):
		for inp, expected in self.TEST_DATA:
			res = highest_three(inp)
			self.assertEqual(res, expected)

if __name__ == '__main__':
	unittest.main()
