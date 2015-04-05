# bring last bit to the front by left shifting rev_num
# set each following bit in rev_num using the right
# shifted num's LSB and the or gate
def reverse_bits(x):
	count = x.bit_length() - 1
	rev_x = x
	x >>= 1
	while x:
		rev_x <<= 1
		rev_x |= (x & 1)
		x >>= 1
		count -= 1

	rev_x <<= count
	return bin(rev_x)

print(reverse_bits(13))

print(bin(13))