def get_best_profit(prices):
	min_price = prices[0]
	max_profit = 0
	for p in prices:
		min_price = min(p, min_price)
		max_profit = max(max_profit, p - min_price)
	return max_profit