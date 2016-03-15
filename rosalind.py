def problem1():
	with open("rosalind_dna.txt") as file:
		data = str(file.read())

	frequency={'A':0, 'C':0, 'G':0, 'T':0}

	for c in data:
		if c != '\n':
			frequency[c] += 1

	for n in "ACGT":
		print(frequency[n], sep=' ')


def problem2():
	with open("rosalind_dna.txt") as file:
		dna = str(file.read())

	i = 0;
	rna = ''

	for c in dna:
		if c == 'T':
			c = 'U'
		
		rna += c

	print(rna)


problem2()
