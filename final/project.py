# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 12:06:38 2016

@author: akirkland, mgarfias
"""
import csv 

def read_data():
    with open("/Users/akirkland/Programming/datascience/final/timesData.csv", 'r', encoding='utf8') as file:
        reader = csv.DictReader(file, delimiter=',')
        rows = [r for r in reader]
    
    top = rows[:50]
    
    

read_data()
