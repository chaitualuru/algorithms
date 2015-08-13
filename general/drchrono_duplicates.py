from collections import OrderedDict

def remove_duplicates(data):
	people = OrderedDict()
	person_per_line = data.split('\n')
	for info in person_per_line[1:]:
		info_pair = info.split(':')
		name = info_pair[0]
		ssn = info_pair[1]
		if ssn in people.iterkeys():
			cur_split_length = len(name.split(' '))
			best_split_length = len(people[ssn].split(' '))
			if cur_split_length > best_split_length:
				people[ssn] = name
			elif cur_split_length == best_split_length:
				if len(name) > len(people[ssn]):
					people[ssn] = name
		else:
			people[ssn] = name
		print people
	for k, v in people.iteritems():
		print v + ':' + k

def main():
	remove_duplicates('9\nm:1\nb,m:1\nm b:1\nb,m c:1\nm c b:1\nl:2\ng:3\nb,g:3\ng b:3')

if __name__ == '__main__':
	main()
