# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 11:37:36 2016

@author: akirkland
"""

def read_fasta(filename):
    """Returns a dictionary associating labels with DNA."""
    result = {}
    with open(filename, 'rt') as f:
        dna = ''
        label = ''
        for line in f:
            if line.startswith('>'):
                if label != '':
                    result[label] = dna
                label = line[1:-1]
                dna = ''
            else:
                dna += line[:-1]
        result[label] = dna
        return result


def overlap(k):
    data = read_fasta("rosalind_grph.txt")         
    for key1 in data:
        for key2 in data:
            if key1 != key2:
                str1 = data[key1]
                str2 = data[key2]  
                
                if str1[:k] == str2[-k:]:
                    print(key2, key1)
                    
        