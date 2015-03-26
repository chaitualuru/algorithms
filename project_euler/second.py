def gen_fib(high = 4000000):
	fib_seq = list([])
	fib_seq.append(1)
	fib_seq.append(2)
	while fib_seq[-1] < high:
		fib_seq.append(fib_seq[-1] + fib_seq[-2])
	fib_seq.pop()
	return fib_seq

def get_sum(fib_seq):
	sum = 0
	for i in fib_seq:
		if i % 2 == 0:
			sum += i
	return sum

print get_sum(gen_fib())