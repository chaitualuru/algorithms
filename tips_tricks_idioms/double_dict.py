from collections import defaultdict
import random

d = defaultdict(lambda: defaultdict(float))

d['hommages']['tributes'] = 10
d['hommages']['tri'] = -1
d['trib']['tri'] = 3
d['fu']['tri'] = 1
d['hommages']['ab'] = 8
d['trib']['cols'] = 9
d['volume']['new'] = 12

st = "a b c"
st1 = " a b b"

def random_numbers(key):
	if key == 'trib':
		return 1
	if key == "fu":
		return 2
	if key == "hommages":
		return 3
	return 0

print max(d.iterkeys(), key = (lambda key: d[key]['tri'] * random_numbers(key)))

print st1.strip().split(" ")