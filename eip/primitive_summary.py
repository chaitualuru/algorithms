# x & 1 will return the LSB of x.
# x & (x - 1) will clear the LSB of x.
# x & !(x - 1) will extract the LSB of x with all other bits cleared.
# x ^ (x >> 1) is the standard (binary-reflected) Gray code for x. 
# xor with all 0's returns the number itself

print (2 | 4)

# Gray code: The problem with natural binary codes is that, with physical, mechanical 
# switches, it is very unlikely that switches will change states exactly in synchrony. 
# In the transition between the two states shown above, all three switches 
# change state. In the brief period while all are changing, the switches will 
# read some spurious position.
# observer cannot tell if that is the "real" position 001, or a transitional state 
# between two other positions. If the output feeds into a sequential system, 
# possibly via combinational logic, then the sequential system may store a false value.