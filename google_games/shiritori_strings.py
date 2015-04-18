from sys import argv

scriptname, filename = argv

with open(filename) as f:
	contents = f.read().splitlines()

def find_chain(lst):
	start = ""
	start_final = ""
	first = True
	num = 1
	num_final = 0
	for i in range(1, len(lst)):
		if lst[i][0] == lst[i - 1][-1]:
			if first:
				first = False
				start = lst[i - 1]
			num += 1
		else:
			print "reached here"
			if num > num_final:
				num_final = num
				start_final = start
			first = True
			num = 1

	return str(num_final) + " " + start_final

print find_chain(contents)