import unittest

def kth_last(head):
	

class KthLastTester(unittest.TestCase):
	TEST_DATA = []

	def run_tests(self):
		for inp, expected in TEST_DATA:
			res = kth_last(inp)
			self.assertEqual(res, expected)

if __name__ == '__main__':
	unittest.main()
