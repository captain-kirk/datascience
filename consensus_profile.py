# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 14:53:55 2016

@author: ARB
"""

def read_FASTA(filename):
    txt = {}
    key = ''
    with open(filename, 'rt') as f:
        for line in f:
            if line.startswith('>'):
                key = str(line[1:len(line)-1])
                txt[key] = ''
            elif line.startswith('>') != True:
                txt[key] += line[:len(line)-1]
                
    dna = list(txt.values())
    
    return dna

def nuc_counter(nuc, matrix):
    
    lst = []
   
    for i in range(len(matrix[0])):
        count = 0
        for row in matrix:
            if row[i] == nuc:
                count+=1
        lst.append(count)
        
    return lst
    
def profile_matrix(matrix):
    
    lst = []
    
    lst.append(nuc_counter('A', matrix))
    lst.append(nuc_counter('C', matrix))
    lst.append(nuc_counter('G', matrix))
    lst.append(nuc_counter('T', matrix))
    
    return lst

def consensus_str(p_matrix):
    
    max_indexes = []
    index_d = {0:'A', 1:'C', 2:'G', 3:'T'}
    
    for i in range(len(p_matrix[0])):
        
        max_val = 0
        max_index = 0
        
        for j in range(len(p_matrix)):
            
            if p_matrix[j][i] >= max_val:
                max_val = p_matrix[j][i]
                max_index = j
                
        max_indexes.append(max_index)
        
    consensus_string = ''
    
    for index in max_indexes:
        consensus_string+=index_d[index]
        
    return consensus_string
    
def print_line(matrix, row):
    
    index_d = {0:'A', 1:'C', 2:'G', 3:'T'}
    
    print("{}:".format(index_d[row]), end = "")
    for i in range(len(matrix[row])):
        print(" {}".format(matrix[row][i]), end = "")
    print()
    
                    
def print_results(matrix):
    
    p_matrix = profile_matrix(matrix)
    c_string = consensus_str(p_matrix)
    
    print(c_string)
    
    for i in range(4):
        print_line(p_matrix, i)
 
    
        
        
    
    
    
    
    
    
    