import csv
import numpy
import math

with open('rosalind_dna.txt') as file:
	dna = str(file.read())

print(dna)

# count = {'A':0, 'C':0, 'G':0, 'T':0}

# for x in dna: 
# 	count[x]+=1

#print(count)