import unittest

def reverse_string(S):
	start = 0
	end = len(S) - 1
	while start != end and end != start + 1:
		S[start], S[end] = S[end], S[start]
		end -= 1
		start += 1
	return S

class ReverseStringTester(unittest.TestCase):
	TEST_DATA = [('a', 'a'),
		('ab', 'ba'),
		('',''),
		('ceul', 'luec'),
		('lol', 'lol')]

	def test_reverse_func(self):
		for inp, expected in self.TEST_DATA:
			res = reverse_string(inp)
			self.assertEqual(res, expected)

if __name__ == '__main__':
	unittest.main()
