# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 11:48:31 2016

@author: akirkland
"""

import math

def nCr(n,r):
    f=math.factorial
    return (f(n)/(f(r)*f(n-r)))

def independentAlles(k,n):
    total= 1-sum([nCr(2**k,i) * .25**i * .75**(2**k-i) for i in range(n)])
    print(total)