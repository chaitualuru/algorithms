# keep track of max_profit by using min_price

def get_max_profit(prices):
	min_price = prices[0]
	cur_price = prices[1]
	max_profit = cur_price - min_price
	
	for index, cur_price in enumerate(prices):
		
		if index < 1:
			continue
		
		min_price = min(min_price, prices[index - 1])
		
		max_profit = max(max_profit, cur_price - min_price)
		
	return max_profit
	

print get_max_profit([5, -12, 17, 19])
		