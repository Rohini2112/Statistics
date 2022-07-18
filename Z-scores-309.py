## 1. Individual Values ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')

houses['SalePrice'].plot.kde(xlim = (houses['SalePrice'].min() , houses['SalePrice'].max()))
plt.axvline(houses['SalePrice'].mean(), label = 'Mean', color = 'Black')
plt.axvline(houses['SalePrice'].std(ddof = 0) + houses['SalePrice'].mean(), color = 'Red', label = 'Standard deviation')
plt.axvline(220000, label = '220000', color = 'Orange')
plt.legend()

very_expensive = False

## 2. Number of Standard Deviations ##

distance = 220000 - houses['SalePrice'].mean()
st_devs_away = distance / houses['SalePrice'].std(ddof = 0)

## 3. Z-scores ##

min_val = houses['SalePrice'].min()
mean_val = houses['SalePrice'].mean()
max_val = houses['SalePrice'].max()

import numpy as np
from numpy import std
def z_score(value, array):
    mean_val = sum(array)/len(array)
    st_dev = std(array, ddof = 0)
    distance = value - mean_val
    
    score = distance / st_dev
    return score

min_z = z_score(min_val, houses['SalePrice'])
mean_z = z_score(mean_val, houses['SalePrice'])
max_z = z_score(max_val, houses['SalePrice'])

## 4. Locating Values in Different Distributions ##

def z_score(value, array, bessel = 0):
    mean = sum(array) / len(array)
    
    from numpy import std
    st_dev = std(array, ddof = bessel)
    
    distance = value - mean
    z = distance / st_dev
    
    return z

north_ames = houses[houses['Neighborhood'] == 'NAmes'] 
clg_creek = houses[houses['Neighborhood'] == 'CollgCr']
old_town = houses[houses['Neighborhood'] == 'OldTown']
edwards = houses[houses['Neighborhood'] == 'Edwards']
somerset = houses[houses['Neighborhood'] == 'Somerst']

L = [north_ames, clg_creek, old_town, edwards, somerset]
d = []

for data in L:
    z = z_score(200000, data['SalePrice'], bessel = 0)
    d.append(z)
    
print(d)    

best_investment = 'College Creek'

## 5. Transforming Distributions ##

mean = houses['SalePrice'].mean()
st_dev = houses['SalePrice'].std(ddof = 0)
houses['z_prices'] = houses['SalePrice'].apply(
    lambda x: ((x - mean) / st_dev)
    )

z_mean_price = houses['z_prices'].mean()
z_stdev_price = houses['z_prices'].std(ddof = 0)

mean_area = houses['Lot Area'].mean()
st_dev_area = houses['Lot Area'].std(ddof = 0)
houses['z_area'] = houses['Lot Area'].apply(lambda x : (x - mean_area)/ st_dev_area)

z_mean_area = houses['z_area'].mean()
z_stdev_area = houses['z_area'].std(ddof = 0)

## 6. The Standard Distribution ##

from numpy import std, mean
population = [0,8,0,8]

mean_pop = sum(population) / len(population)
stdev_pop = std(population, ddof = 0)

z_pop = []
for value in population:
    z = (value - mean_pop) / stdev_pop
    z_pop.append(z)
    
mean_z = sum(z_pop) / len(z_pop)
stdev_z = std(z_pop, ddof = 0)

## 7. Standardizing Samples ##

from numpy import std, mean
sample = [0,8,0,8]

x_bar = mean(sample)
s = std(sample, ddof = 1)

standardized_sample = []
for value in sample:
    z = (value - x_bar) / s
    standardized_sample.append(z)
    
stdev_sample = std(standardized_sample, ddof = 1)

## 8. Using Standardization for Comparisons ##

mean_index1 = houses['index_1'].mean()
stdev_index1 = houses['index_1'].std(ddof = 0)
mean_index2 = houses['index_2'].mean()
stdev_index2 = houses['index_2'].std(ddof = 0)

houses['z_1'] = houses['index_1'].apply(lambda x : (x - mean_index1) / stdev_index1)

houses['z_2'] = houses['index_2'].apply(lambda x : (x - mean_index2) / stdev_index2)

print(houses[['z_1', 'z_2']].head(2))
better = 'first'

## 9. Converting Back from Z-scores ##

transformed = []
for val in houses['z_merged']:
    t = (val*10)+50
    transformed.append(t)
    
houses['transformed'] = transformed

mean_transformed = houses['transformed'].mean()
stdev_transformed = houses['transformed'].std(ddof = 0)