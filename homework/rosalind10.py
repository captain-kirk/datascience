"""
Created on Tue Mar 8 8:37:16 2016

@author: akirkland & michellegarfias
"""

import csv
import numpy as np

with open ('rosalind_cons.txt') as f:
	data = [list(line) for line in f if line[0] != '>']

#dna = numpy.asarray(data)

results = []

for i in range(len(data[0])-1):
	acount = ccount = gcount = tcount = 0
	for j in range(len(data)):
		if (data[j][i]) == 'A':
			acount += 1
		elif (data[j][i]) == 'C':
			ccount += 1
		elif (data[j][i]) == 'G':
			gcount += 1
		elif (data[j][i]) == 'T':
			tcount += 1
	print()

	col = [acount, ccount, gcount, tcount]
	results.append(col)
	print(results)

ans = np.array(results)

print(ans[0][3])


		

