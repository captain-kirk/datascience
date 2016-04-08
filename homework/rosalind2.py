def problem2():
	with open("rosalind_rna-2.txt") as file:
		dna = str(file.read())

	rna = ''

	for c in dna:
		if c == 'T':
			c = 'U'
		
		rna += c

	print(rna)

problem2()