import unittest

def reverse_string(S):
    start = 0
    end = len(S) - 1
    st_list = list(S)
    while start != end and start != end + 1:
        st_list[start], st_list[end] = st_list[end], st_list[start]
        end -= 1
        start += 1
    return ''.join(st_list)

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
