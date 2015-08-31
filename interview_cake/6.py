import unittest

def get_intersection(R1, R2):
	r1_xlow = R1['x']
	r1_xhigh = r1_xlow + R1['w']
	r1_ylow = R1['y']
	r1_yhigh = r1_ylow + R1['h']
	r2_xlow = R2['x']
	r2_xhigh = r2_xlow + R2['w']
	r2_ylow = R2['y']
	r2_yhigh = r2_ylow + R2['h']

	if r1_xlow >= r2_xhigh or r1_xhigh <= r2_xlow or r1_ylow >= r2_yhigh or r1_yhigh <= r2_ylow:
		return "There is no intersection."

	result_xlow = max(r1_xlow, r2_xlow)
	result_xhigh = min(r1_xhigh, r2_xhigh)
	result_ylow = max(r1_ylow, r2_ylow)
	result_yhigh = min(r1_yhigh, r2_yhigh)

	return {'x': result_xlow, 'y': result_ylow, 'w': result_xhigh - result_xlow, 'h': result_yhigh - result_ylow}

class RectangleIntersectionTester(unittest.TestCase):
	TEST_DATA = [(({'x': 1, 'y': 5, 'w': 5, 'h': 10}, {'x': 3, 'y': 6, 'w': 3, 'h': 3}), {'x': 3, 'y': 6, 'w': 3, 'h': 3}),
		(({'x': 2, 'y': -3, 'w': 2, 'h': 3}, {'x': 7, 'y': 10, 'w': 2, 'h': 3}), "There is no intersection.")]

	def test(self):
		for inp, expected in self.TEST_DATA:
			res = get_intersection(inp[0], inp[1])
			self.assertEqual(res, expected)

if __name__ == '__main__':
	unittest.main()
