"""Apple Stocks"""

def max_profit(stocks):
    """Return the maximum profit attainable from 1 buy and 1 sell of stocks."""
    if not stocks or len(stocks) == 1:
        return None
    lowest_so_far = stocks[0]
    cur_max = stocks[1] - lowest_so_far
    for stock in stocks[2:]:
        cur_max = max(cur_max, stock - lowest_so_far)
        lowest_so_far = min(lowest_so_far, stock)
    return cur_max

def main():
    """Entry point for the program."""
	# constraints: cannot buy before selling, cannot buy and sell at the same timestep
	# None
    print max_profit([10])
	# 12
    print max_profit([10, 22])
	# -2
    print max_profit([10, 8])
	# 0
    print max_profit([10, 10])
	# 32
    print max_profit([2, 5, 1, 12, 3, 33])
	# 48
    print max_profit([24, 10, 3, 12, 25, 3, 7, 12, 50, 51, 32, 49])

if __name__ == '__main__':
    main()
