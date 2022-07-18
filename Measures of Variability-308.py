## 1. The Range ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')

def range(array):
    r = max(array) - min(array)
    return r

range_by_year = {}
for year in houses['Yr Sold'].unique():
    data_by_year = houses[houses['Yr Sold'] == year]
    range_by_year[year] = range(data_by_year['SalePrice'])

one = False
two = True
    
    
        

## 2. The Average Distance ##

C = [1,1,1,1,1,1,1,1,1,21]

def avg_dis(array):
    distances = []
    mean = sum(array) / len(array)
    for val in array:
        dis = val - mean
        distances.append(dis)
    return sum(distances) / len(distances)

avg_distance = avg_dis(C)
print(avg_distance)
        

## 3. Mean Absolute Deviation ##

C = [1,1,1,1,1,1,1,1,1,21]

def mean_absolute_deviation(array):
    distances = []
    mean = sum(array) / len(array)
    for val in array:
        dis = abs(val - mean)
        distances.append(dis)
    return sum(distances) / len(distances)

mad = mean_absolute_deviation(C)

## 4. Variance ##

C = [1,1,1,1,1,1,1,1,1,21]

def variance(array):
    distances = []
    mean = sum(array) / len(array)
    for val in array:
        dis = (val - mean)**2
        distances.append(dis)
    return sum(distances) / len(distances)

variance_C = variance(C)

## 5. Standard Deviation ##

from math import sqrt
C = [1,1,1,1,1,1,1,1,1,21]

def standard_deviation(array):
    distances = []
    mean = sum(array) / len(array)
    for val in array:
        dis = (val - mean)**2
        distances.append(dis)
    return sqrt(sum(distances) / len(distances))

standard_deviation_C = standard_deviation(C)

## 6. Average Variability Around the Mean ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
        
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

d = {}
for year in houses['Yr Sold']:
    year_segment = houses[houses['Yr Sold'] == year]
    s = standard_deviation(year_segment['SalePrice'])
    d[year] = s
    
greatest_variability = 2006
lowest_variability = 2010
    
    

## 7. A Measure of Spread ##

sample1 = houses['Year Built'].sample(50, random_state = 1)
sample2 = houses['Year Built'].sample(50, random_state = 2)

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

bigger_spread = 'sample 2'

st_dev1 = standard_deviation(sample1)
st_dev2 = standard_deviation(sample2)

## 8. The Sample Standard Deviation ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

import matplotlib.pyplot as plt

st_devs = []
for i in range(5000):
    s = houses['SalePrice'].sample(10, random_state = i)
    st_dev = standard_deviation(s)
    st_devs.append(st_dev)

plt.hist(st_devs)
plt.axvline(standard_deviation(houses['SalePrice']))
    
    
    
    
    

## 9. Bessel's Correction ##

from math import sqrt
def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / (len(distances)-1)
    
    return sqrt(variance)

import matplotlib.pyplot as plt
st_devs = []

for i in range(5000):
    sample = houses['SalePrice'].sample(10, random_state = i)
    st_dev = standard_deviation(sample)
    st_devs.append(st_dev)

plt.hist(st_devs)
plt.axvline(pop_stdev)  # pop_stdev is pre-saved from the last screen

## 10. Standard Notation ##

sample = houses.sample(100, random_state = 1)
from numpy import std, var

pandas_stdev = sample['SalePrice'].std(ddof = 1)
numpy_stdev = std(sample['SalePrice'], ddof = 1)

equal_stdevs = pandas_stdev == numpy_stdev

pandas_var = sample['SalePrice'].var(ddof = 1)
numpy_var = var(sample['SalePrice'], ddof = 1)

equal_vars = pandas_var == numpy_var

## 11. Sample Variance — Unbiased Estimator ##

population = [0, 3, 6]

samples = [[0,3], [0,6],
           [3,0], [3,6],
           [6,0], [6,3]
          ]

from numpy import var, std

pop_var = var(population, ddof = 0)
pop_std = std(population, ddof = 0)

st_devs = []
variances = []

for sample in samples:
    st_devs.append(std(sample, ddof = 1))
    variances.append(var(sample, ddof = 1))
    
mean_std = sum(st_devs) / len(st_devs)
mean_var = sum(variances) / len(variances)

equal_stdev = pop_std == mean_std
equal_var = pop_var == mean_var