# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 12:48:07 2016

@author: harrisonforch
"""

from matplotlib import pyplot as plt
import csv

def global_mean_temp():
    
    with open('annual.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        rows = [r for r in reader if r[0] == 'GCAG']
        years = [row[1] for row in rows]
        temps = [row[2] for row in rows]
        plt.plot(years, temps)
        plt.title('Global Mean Temperatures')
        plt.xlabel('Year')
        plt.ylabel('Difference from 20th century average ('
        + u'\N{DEGREE SIGN}' + 'C)')
        plt.show()
    
def global_carbon_emissions():
    with open('global.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        rows = [r for r in reader]
        years = [row[0] for row in rows]
        total = [row[1] for row in rows]
        plt.plot(years, total)
        plt.title('Global CO2 Emissions')
        plt.xlabel('Year')
        plt.ylabel('Total Carbon Emissions')
        plt.show()
        
def guns_shit():
    with open('guns.csv', 'r', encoding = "utf-8") as f: 
        reader = csv.DictReader(f, delimiter=',') 
        rows = [r for r in reader if r['Average firearms per 100 people'] != '']
    decreasing = sorted(rows, key=rate, reverse=True)
    decreasing = decreasing[:20]
    countries=[country(row) for row in decreasing]
    values=[rate(row) for row in decreasing]
    
    xs = [i + 0.1 for i, _ in enumerate(countries)]
    
    plt.bar(xs,values)
    plt.ylabel("Deaths by Firearms per 100 people")
    plt.title("Deaths by Firearms per 100 by Country")
    plt.xticks([i + 0.5 for i, _ in enumerate(countries)], countries)
    plt.show()

def rate(row):
    return float(row['Average firearms per 100 people'])
def country(row):
    return str(row['ISO code'])
    
def iris():
    with open('iris.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        rows = [r for r in reader]
        print(rows)
    sepal_length = [row[r][0] for row in rows]
    sepal_width = [row[r][1] for row in rows]
    iris_type= [row[r][4] for row in rows]
    
    
    plt.scatter(sepal_length,sepal_width)
    
    for label, sepal_length_count, sepal_width_count in zip(iris_type,sepal_length,sepal_width):
        plt.annotate(iris_type,sy=(sepal_length_count,sepal_width_count),xytext=(5,-5),textcoords='ofset points')
    plt.title("Sepal Iris Width vs Length")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Sepal Width (cm)")
    plt.show()