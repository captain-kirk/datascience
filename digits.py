# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 11:36:36 2016

@author: akirkland
"""

import numpy as np
from sklearn import datasets

digits = datasets.load_digits()
digits_X = digits.data
digits_y = digits.target
np.unique(digits_y)

np.random.seed(0)
indices = np.random.permutation(len(digits_X))
digits_X_train = digits_X[indices[:-100]]
digits_y_train = digits_y[indices[:-100]]
digits_X_test = digits_X[indices[-100:]]
digits_y_test = digits_y[indices[-100:]]

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(digits_X_train, digits_y_train)

import matplotlib.pyplot as plt

#Load the digits dataset
digits = datasets.load_digits()

#Display the first digit
#plt.figure(1, figsize=(3, 3))
#plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation='nearest')
#plt.show()

def results():
    
    for i in range(1,51):
        knn = KNeighborsClassifier(i)
        knn.fit(digits_X_train,digits_y_train)
        a = knn.predict(digits_X_test)
        b = digits_y_test
        print(accuracy(a,b))
        

def accuracy(a, b):
    count = 0;
    
    for x in range(0, len(a)):
        if a[x] == b[x]:
            count += 1
            
    return count/len(a)
    

#Values of k from 1-5, 7-10, 14-23 are 100% accurate. For k values of 24 and greater, accuracy decreases.