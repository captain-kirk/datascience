def problem1():
	with open("rosalind_dna.txt") as file:
		data = str(file.read())

	frequency={'A':0, 'C':0, 'G':0, 'T':0}

	for c in data:
		if c != '\n':
			frequency[c] += 1

	for n in "ACGT":
		print(frequency[n], end=' ')


problem1()





