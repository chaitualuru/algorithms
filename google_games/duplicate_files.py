from sys import argv

scriptname, filename = argv

with open(filename) as f:
    contents = f.read().splitlines()

unique_set = set([])

for c in contents:
    line = c.split(" ")
    md5 = line[0]
    size = line[1]
    info = md5 + " " + size
    if info not in unique_set:
        unique_set.add(info)

print len(unique_set)
