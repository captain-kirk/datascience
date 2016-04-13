# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 12:39:40 2016

@author: akirkland
"""

def expoff(a,b,c,d,e,f):
    prob1 = 1
    prob2 = .75
    prob3 = .5
    prob4 = 0
    
    ans = prob1*a*2 + prob1 * b *2 + prob1 * c *2 + prob2 * d *2 + prob3 * e *2 + prob4 * f *2
    
    print(ans)
    