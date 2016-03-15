"""
Created on Fri Feb 26 11:42:14 2016

@author: akirkland & michellegarfias
"""

def problem7(a, b, c):
	total = a + b + c
	dom = a / total
	het = b / total
	rec = c / total

	#cross homoD with other stuff
	domdom = dom*((a-1)/(total-1))
	domhet = dom*((b) / (total-1))
	domrec = dom*((c) / (total - 1))

	#cross het with other stuff
	hetdom = het*((a) / (total - 1))
	hethet = het*((b-1)/(total-1))
	hetrec = het*((c) / (total - 1))

	#cross homoR with other stuff
	recdom = rec*((a)/(total-1))
	rechet = rec*((b)/(total-1))


	prob = domdom + domhet + domrec + hetdom + 0.75*hethet + 0.5*hetrec + recdom + 0.5*rechet

	print(prob) 


problem7(28,24,19)