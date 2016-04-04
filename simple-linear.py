q# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 14:06:19 2016

@author: drake
"""

import random
import matplotlib.pyplot as plt

true_alpha = 0.3
true_beta = 0.2
def true_y(x):
    return true_beta * x + true_alpha +  random.gauss(0, 1)

xs = [random.uniform(0, 20) for i in range(100)]
ys = [true_y(x) for x in xs]

plt.scatter(xs, ys)

import simple_linear_regression

alpha, beta = simple_linear_regression.least_squares_fit(xs, ys)

def predict(x):
    return beta * x + alpha

plt.plot([0, 20], [predict(0), predict(20)])
plt.show()
