# How would you go about computing the parity of a very large number of 64-bit 
# nonnegative integers?

def check_parity(num):
	count = 0
	for i in bin(num):
		if i == '1':
			count += 1
	return bool(count % 2)

# (num&1) will tell us if the LSB is 0 or 1. then xor result will behave as the
# check to see if 1 is seen odd or even number of times
def check_parity2(num):
	result = 0
	while num:
		result ^= (num & 1)
		num >>= 1
	return bool(result)