from functools import wraps

# a decorator is generally a function that takes another function as an argument and 
# returns a new function, that can be used just like the initial function, but presumably
# ith some extra logic
def square(func):
	@wraps(func)
	def _square(num):
		return func(num) ** 2
	return _square

# the above can be used as following
@square
def plus(num):
	return num + 1

print plus(3)
