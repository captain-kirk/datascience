# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 15:10:11 2016

@author: harrisonforch
"""
import numpy as np
f = open('rosalind_cons.txt', 'r')
lines = f.read().splitlines()
#print(lines)


sequences=[]
temp=[]
for line in lines:
    if line[0]=='>' and len(temp)>0:
       sequences.append(temp) 
       temp=[]
    else:  
        for c in line:
            if c=='A' or c=='C' or c=='G' or c=='T':
                temp.append(c)
sequences.append(temp)
#print(sequences)
        
nSeq=np.array(sequences)
x=np.zeros((4,len(nSeq[0])),np.dtype(int))
i=0
for colum in nSeq.T:
    for c in colum:
        if c=='A':
            x[0][i]+=1
        elif c=='C':
            x[1][i]+=1
        elif c=='G':
            x[2][i]+=1
        elif c=='T':
            x[3][i]+=1
    i+=1


consensus=""
            
for i in range(0,len(x[0])):
    if x[0][i]>=x[1][i]and x[0][i]>= x[2][i] and x[0][i]>=x[3][i]:
        consensus+='A'
    elif x[1][i]>=x[0][i]and x[1][i]>= x[2][i] and x[1][i]>=x[3][i]:
        consensus+='C'
    elif x[2][i]>=x[0][i]and x[2][i]>= x[1][i] and x[2][i]>=x[3][i]:
        consensus+='G'
    elif x[3][i]>=x[1][i]and x[3][i]>= x[2][i] and x[3][i]>=x[0][i]:
        consensus+='T'


with open("ros_submit.txt", 'w') as f:
	f.write(consensus)
	i = 0
	for d in x:
		#print(d)
		if(i==0):
			f.write("\n")
			f.write("A: ")
		elif i==1:
			f.write("\n")
			f.write("C: ")
		elif i==2:
			f.write("\n")
			f.write("G: ")
		elif i==3:
			f.write("\n")
			f.write("T: ")
		for j in d:
			f.write(str(j))
			f.write(" ")
		i+=1