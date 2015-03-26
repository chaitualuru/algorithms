def gen_factors(num = 600851475143):
	factors = list([])
	for i in range(1, num):
		if num % i == 0:
			factors.append(i)
	return factors

print gen_factors()