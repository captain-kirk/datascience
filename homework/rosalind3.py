
def problem3():
	with open ('test2.txt') as file:
		dna = str(file.read())

	print(dna)
	dna = dna[::-1];
	revc = ''

	print (dna)

	for c in dna:
		if c == 'T':
			c = 'A'
		elif c == 'A':
			c = 'T'
		elif c == 'G':
			c = 'C'
		elif c == 'C':
			c = 'G'
		
		revc += c

	print (revc)


problem3()