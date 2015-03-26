from random import randint

def rand5():
	x = randint(1, 7)
	return x if x <= 5 else rand5()

def rand5_other():
	result = 7
	while result > 5:
		result = randint(1, 7)
	return result

print rand5_other()