# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
    years = [row[1] for row in rows]
    temp = [row[2] for row in rows]
    plt.plot(years, temp)
    plt.title('Global Mean Temperatures')
    plt.xlabel('Year')
    plt.ylabel('Difference from 20th century average ('
        + u'\N{DEGREE SIGN}' + 'C)')
    plt.show()

def guns():
    with open('guns.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=',')
        rows = [r for r in reader if r['Average firearms per 100 people'] != '']
        
    decreasing = sorted(rows, key=rate, reverse=True)
    decreasing = decreasing[:20]
        
    countries = [country['ISO code'] for country in decreasing]
    rates = [row['Average firearms per 100 people'] for row in decreasing]

    i=0;
    
    floatValues = []
    for item in rates:
        floatValues.append(float(rates[i]))
        i+=1
             
    xs = [i + 0.1 for i, _ in enumerate(countries)]
        
    plt.bar(xs, floatValues)
    plt.ylabel("Deaths by Firearms per 100 people")
    plt.title("Deaths by Firearms per 100 by Country")
    plt.xticks([i + 0.5 for i, _ in enumerate(countries)], countries)
    plt.show()

def rate(row):
    return float(row['Average firearms per 100 people'])
    
    
def iris():
    with open('iris.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        rows = [r for r in reader]        
        
    length = [row[0] for row in rows]
    width = [row[1] for row in rows]   
    
    plt.scatter(length, width)
    plt.title("Iris Sepal Length vs Sepal Width") 
    plt.xlabel("Sepal Length")
    plt.ylabel("Sepal Width")
    plt.show()

