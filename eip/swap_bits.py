# swap bits at positons i and j in x

def swap_bits(x, i, j):
	i_bit = (x >> i) & 1
	j_bit = (x >> j) & 1
	if i_bit != j_bit:
		x ^= (1 << i) | (1 << j)
	return x

print swap_bits(5, 1, 2)