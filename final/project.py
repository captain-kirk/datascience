# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 12:06:38 2016

@author: akirkland, mgarfias
"""
import csv 
import math
from matplotlib import pyplot as plt

def mean(list):
	return sum(list)/float(len(list))

def read_data():
    with open("/Users/akirkland/Programming/datascience/final/timesData.csv", 'r', encoding='utf-8', errors="ignore") as file:
        reader = csv.DictReader(file, delimiter=',')
        rows = [r for r in reader]
        
    top = rows[:200]

    
    name = [school['university_name'] for school in top]
    fmr = [ratio['female_male_ratio'] for ratio in top] 
    incomes = [income['income'] for income in top]
    ranks = [rank['world_rank'] for rank in top]
    location = [country['country'] for country in top]
      
    
#   dictionary of countries and top university count
    location_tracker = {}
    for place in location:
        if place in location_tracker:
            location_tracker[place] += 1
        else:
            location_tracker[place] = 1
  
  
#   make a lookup table that contains country ISO codes
#   this will allow labeling in the graph
    with open('/Users/akirkland/Programming/datascience/final/ISO.csv', 'r', encoding='utf-8', errors="ignore") as file:
        reader = csv.DictReader(file, delimiter=",")
        codes = [r for r in reader]

    lookup = {}
    for pair in codes:
        lookup[pair['country']] = pair['code']
    
    countries = []
    count = []        

    for key in location_tracker.keys():
        countries.append(lookup[key])
        count.append(location_tracker[key])
             
    xs = [i + 0.1 for i, _ in enumerate(countries)]
        
    plt.figure(figsize=(20,10))
    plt.bar(xs, count)
    plt.xlabel("Country")
    plt.ylabel("Number of Top Universities")
    plt.title("Location of Top 200 Universities")
    plt.xticks([i + 0.5 for i, _ in enumerate(countries)], countries)
    plt.show()

#   make a graph that maps countries to percentage of international students
    cleaned = []
    for school in top:
        if school['international_students'] != '':
            cleaned.append(school)
    
#    intl = [float(perc['international_students'].replace('%','')) for perc in cleaned]

#    print(intl)

    international = {}      
    
#   get average of international students in each country in the top 200
    for key in location_tracker:
        international[key] = 0;
        values = []
        for school in cleaned:
            if school['country'] == key:
                values.append(float(school['international_students'].replace('%','')))
        international[key]=(mean(values))
    
    avg = []
    countries = []
    for key in international:
        avg.append(international[key])
        countries.append(lookup[key])
        
    xs = [i + 0.1 for i, _ in enumerate(countries)]
        
    plt.figure(figsize=(20,10))
    plt.bar(xs, avg)
    plt.xlabel("Country")
    plt.ylabel("Average Amount of International Students (%)")
    plt.title("Average Percentage of International Students at Top Universities in Various Countries")
    plt.xticks([i + 0.5 for i, _ in enumerate(countries)], countries)
    plt.show()           
        


#   female to male ration for top ranking universities
    ratio = []
    rank = []    
    
    for school in top:
        str = school['female_male_ratio']
        if str != '':
            ratio.append(float(str[:2]))
            rank.append(school['world_rank'])
     
    plt.scatter(rank, ratio)
    plt.title('World Rank vs. Percentage of Female Students')
    plt.xlabel('Rank')
    plt.ylabel('Percentage of Female Students')
    plt.show()

    bar = {
        10 : 0,
        20: 0,
        30: 0,
        40: 0,
        50: 0,
        60: 0,
        70: 0,
        80: 0,
        90: 0,
        100: 0
    }
    
    for num in ratio:
        for key in bar:
            if num <= key and num > (key-10):
                bar[key] += 1
    
    values = []
    for i in range(10, 101, 10):
        values.append(bar[i])
    
    labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100']    
    
    xs = [i + 0.1 for i, _ in enumerate(labels)]
        
    plt.bar(xs, values)
    plt.xlabel("Percentage of Females in Student Body")
    plt.ylabel("Number of Universities in Range")
    plt.xticks([i + 0.5 for i, _ in enumerate(labels)], labels)
    plt.show()

#   maps rank to income 
    cleaned = []
    for school in top:
        if school['income'] != '-':
            cleaned.append(school)
            
    incomes = [income['income'] for income in cleaned]
    ranks = [rank['world_rank'] for rank in cleaned]

    plt.scatter(ranks, incomes)
    plt.title('World Rank vs. Income')
    plt.xlabel('Rank')
    plt.ylabel('Income (millions)')
    plt.show()
    

#   maps rank to number of students
    cleaned = []
    
    for school in top :
        if school['num_students'] != '':
            cleaned.append(school)
            
    
    rank = [rank['world_rank'] for rank in cleaned]
    size = [int(population['num_students'].replace(',','')) for population in cleaned] 
    
    labels = ['Small (0-5000)', 'Medium (5000-15000)', 'Large (15000+)']
    values = []

    i = 0;    
    for num in size:
        if num <= 5000:
            i += 1
    values.append(i)
    
    i = 0;
    for num in size:
        if num > 5000 and num < 15000:
            i+=1
    values.append(i)
    
    i = 0;
    for num in size:
        if num >= 15000:
            i+=1
    values.append(i)
    
    xs = [i + 0.1 for i, _ in enumerate(labels)]
    
    plt.scatter(rank, size)
    plt.title('World Rank vs. Student Body Size')
    plt.xlabel("Rank")
    plt.ylabel("Student Body Size")
    plt.show()
        
    plt.bar(xs, values)
    plt.xlabel("Size of Universities")
    plt.ylabel("Number of Universities in Range")
    plt.xticks([i + 0.5 for i, _ in enumerate(labels)], labels)
    plt.show()
    
    plt.figure()
    plt.boxplot(size, 0, '')
    plt.title('Distribution Display for Student Body Size')
    plt.ylabel('Number of Students')
    plt.show()
            
    
#   map size to student to faculty ratio
    cleaned = []
    for school in top:
        str1 = school['student_staff_ratio']
        str2 = school['num_students']
        if str1 != '' and str2 != '':
            cleaned.append(school)
            
    size = [int(population['num_students'].replace(',','')) for population in cleaned]
    ratio = [float(studentstaff['student_staff_ratio'].replace(',','')) for studentstaff in cleaned]

    plt.scatter(size, ratio)
    plt.title('Student Body Size vs. Student Staff Ratio')
    plt.xlabel('Student Body Size')
    plt.ylabel('Student-Staff Ratio')
    plt.show()
    
#   box plot of student staff ratio
    plt.figure()
    plt.boxplot(ratio, 0, '')
    plt.title('Distribution Display for Student-Staff Ratio')
    plt.ylabel('Students Per Faculty Member')
    plt.show()

        
read_data()
