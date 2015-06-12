import sys

class Fibonacci:
	def dict_get_nth(self, n):
		if n < 0:
			raise KeyError("Not a valid number.")
		fib = {}
		fib[0] = 0
		fib[1] = 1
		for i in range(2, n + 1):
			fib[i] = fib[i - 1] + fib[i - 2]
		return fib[n]

	def get_nth(self, n):
		if n < 0:
			raise TypeError("No negative numbers.")
		if (n <= 1):
			return n
		prev = 1
		prev_prev = 0
		cur = 0
		for i in range(2, n + 1):
			cur = prev + prev_prev
			prev_prev = prev
			prev = cur

		return cur

def main():
	fib = Fibonacci()

	# 0 -> 0
	print fib.dict_get_nth(0)

	# 1 -> 1
	print fib.dict_get_nth(1)

	# 5 -> 5
	print fib.dict_get_nth(5)

	# 6 -> 8
	print fib.dict_get_nth(6)

	# 0 -> 0
	print fib.get_nth(0)

	# 1 -> 1
	print fib.get_nth(1)

	# 5 -> 5
	print fib.get_nth(5)

	# 6 -> 8
	print fib.get_nth(6)

	# -1 -> KeyError
	print fib.get_nth(-1)

if __name__ == '__main__':
	sys.exit(main())