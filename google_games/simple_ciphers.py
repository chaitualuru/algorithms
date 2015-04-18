from sys import argv

scriptname, cipher_text, word_list = argv

with open(filename) as f:
	contents = f.read().splitlines()

for c in contents:
