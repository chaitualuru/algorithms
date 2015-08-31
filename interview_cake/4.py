import unittest

def merge_meetings(M):
	M.sort()
	res_start = M[0][0]
	res_end = M[0][1]
	result = list([])
	for meeting in M[1:]:
		start = meeting[0]
		end = meeting[1]
		if res_end >= start:
			if res_end < end:
				res_end = end
		else:
			result.append((res_start, res_end))
			res_start = start
			res_end = end

	result.append((res_start, res_end))

	return result


class MergeMeetingsTester(unittest.TestCase):
	TEST_DATA = [
		([(0,2),(3,5),(7,8),(1,7)], [(0,8)])]

	def test(self):
		for inp, expected in self.TEST_DATA:
			res = merge_meetings(inp)
			self.assertEqual(res, expected)

if __name__ == '__main__':
	unittest.main()
