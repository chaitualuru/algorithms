import unittest

def check_uniqueness_ds(S):
	return len(set(S)) == len(S)

def check_uniqueness(S):
	for char in S:
		if S.count(char) > 1:
			return False
	return True

class UniquenessTester(unittest.TestCase):
	TEST_DATA = [
		('a', True),
		('aa', False),
		('ab', True),
		('ab ', True),
		('', True),
		('  ', False),
		('asdoifjg', True),
		('asdoifji', False)]

	def test_uniqueness_funcs(self):
		for S, expected in self.TEST_DATA:
			res1 = check_uniqueness_ds(S)
			self.assertEqual(res1, expected)

			res2 = check_uniqueness(S)
			self.assertEqual(res2, expected)

if __name__ == '__main__':
	unittest.main()
