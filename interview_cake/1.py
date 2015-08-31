import unittest

def max_profit(S):
	if len(S) < 2:
		raise IndexError('Geting a profit requires at least 2 prices')
	buy = S[0]
	sell = S[1]
	profit = sell - buy
	lowest = min(buy, sell)
	for stock in S[1:]:
		profit = max(stock - lowest, profit)
		lowest = min(stock, lowest)
	return profit

class MaxProfitTester(unittest.TestCase):
	TEST_DATA = [
		([3,3,3,3,3], 0),
		([2, 3, 12], 10),
		([12, 2, 3, 7], 5)]

	def test(self):
		for inp, expected in self.TEST_DATA:
			res = max_profit(inp)
			self.assertEqual(res, expected)

if __name__ == '__main__':
	unittest.main()
