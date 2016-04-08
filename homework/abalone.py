# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 11:42:14 2016

@author: akirkland & michellegarfias
"""

from matplotlib import pyplot as plt
import csv
import math
import numpy

def mean(list):
	return sum(list)/float(len(list))

def standardDeviation(list):
	return math.sqrt(sum([(x - mean(list))*(x-mean(list)) for x in list])/(float(len(list))-1))

def median(x):
	sortedX = sorted(x)
	mid = len(x) // 2

	if len(x)%2 == 1:
		return sortedX[mid]
	else:
		lo = mid - 1
		hi = mid
		return (sortedX[lo] + sortedX[hi]) / 2

def de_mean(list):
	a = mean(list)
	return [x - a for x in list]

def covariance(x, y):
	return numpy.dot(de_mean(x), de_mean(y))/(len(x) - 1)

def coorelation(x, y):
	stdx = standardDeviation(x)
	stdy = standardDeviation(y)
	if stdx > 0 and stdy > 0:
		return covariance(x, y) / stdx / stdy
	else:
		return 0

#Main
with open('abalone.data.txt', 'r') as f:
	reader = csv.reader(f, delimiter = ',')
	rows = [r for r in reader]

sex = [row[0] for row in rows]
length = [float(row[1]) for row in rows]
rings = [int(row[8]) for row in rows]

print(length)

print("Mean number of rings: %lf" %mean(rings))
print("Median number of rings: %d" %median(rings))
print("Standard deviation of number of rings: %lf" %standardDeviation(rings))
print("Coorelation between length and rings: %lf" %coorelation(length, rings))

count = 0
for s in sex: 
	if s == 'M':
		count += 1
pMale = count/len(sex)
print("P[male]: %lf" %pMale)

count = 0
for l in length:
	if l > mean(length):
		count += 1
pLarge = count/len(sex)
print("P[large]: %lf" %pLarge)

# count = 0
# for s, l in zip(sex, length):
# 	if s == 'M' and l > mean(length):
# 		count += 1

count = 0
for i in range(0, len(sex)):
	if sex[i]=='M' and length[i] > mean(length):
		count += 1
print("P[male and large]: %lf" %(count/len(sex)))

# count = 0
# for s, l in zip(sex, length):
# 	if s == 'M' or l > mean(length):
# 		count += 1

count = 0
for i in range(0, len(sex)):
	if sex[i] == 'M' or length[i] > mean(length):
		count += 1
		
print("P[male or large]: %lf" %(count/len(sex)))

pMaleLarge = (pMale*pLarge)/pLarge
print("P[male | large: %lf" %pMaleLarge)

pLargeMale = (pMale*pLarge)/pMale
print("P[large | male]: %lf" %pLargeMale)