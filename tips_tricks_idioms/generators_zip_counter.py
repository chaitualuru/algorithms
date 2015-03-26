import random
from collections import Counter

# set
colors = {'red', 'green', 'blue', 'yellow', 'orange', 'black', 'white', 'red'}

input_values = {'red', 'black', 'pizza'}

valid_values = input_values.intersection(colors)

print valid_values

invalid_values = input_values.difference(colors)

print invalid_values

# if not input_values.issubset(colors):
	# raise ValueError("Invalid color - " + ", ".join(invalid_values))

# for... else requires break

# list comprehension
numbers = list(range(100))
mul = [num * 3 if num % 2 else num * 2 for num in numbers]

# generators
squares = (num * num for num in xrange(100))

total = 0
for i in squares:
	total += i

print total

# using yield
def random_numbers(high = 1000):
	while True:
		yield random.randint(0, high)

print random_numbers().next()

# dictionary comprehension
teachers = {
	'Andy': 'English',
	'Joan': 'Mathematics',
	'Alice': 'Computer Science'
}

subjects = {subject: teacher for teacher, subject in teachers.items()}
print subjects

# zip
names = ('James', 'Andrew', 'Mark')
for i, name in zip(random_numbers(), names):
	print i, name

print dict(zip(names, random_numbers()))

# Counter 
order = (
    ('Mark', 'Steak'),
    ('Andrew', 'Veggie Burger'),
    ('James', 'Steak'),
    ('Mark', 'Beer'),
    ('Andrew', 'Beer'),
    ('James', 'Wine'),
)

order_count = Counter(menu_item for name, menu_item in order)
print order_count