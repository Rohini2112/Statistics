## 2. The Mean ##

distribution = [0,2,3,3,3,4,13]
mean = sum(distribution)/len(distribution)
center = False
below = []
above = []

for val in distribution:
    if val < mean:
        below.append(mean - val)
    else:
        above.append(val - mean)
        
equal_distances = (sum(below) == sum(above))

## 3. The Mean as a Balance Point ##

from numpy.random import randint, seed
equal_distances = 0

for i in range(5000):
    seed(i)
    distribution = randint(0, 1000, 10)
    mean = sum(distribution)/len(distribution)
    
    below = []
    above = []

    for val in distribution:
        if val < mean:
            below.append(mean - val)
        else:
            above.append(val - mean)
        
    if round((sum(below)), 1) == round((sum(above)), 1):
        equal_distances += 1

## 4. Defining the Mean Algebraically ##

one = False
two = False
three = False

## 5. An Alternative Definition ##

distribution_1 = [42, 24, 32, 11]
distribution_2 = [102, 32, 74, 15, 38, 45, 22]
distribution_3 = [3, 12, 7, 2, 15, 1, 21]

def mean(distribution):
    total = 0
    length = len(distribution)
    for val in distribution:
        total += val
    return total / length

mean_1 = mean(distribution_1)
mean_2 = mean(distribution_2)
mean_3 = mean(distribution_3)
        

## 6. Introducing the Data ##

import pandas as pd

houses = pd.read_table('AmesHousing_1.txt')
h = houses.head()
s = houses.shape

one = True
two = False
three = True

## 7. Mean House Prices ##

def mean(distribution):
    sum_distribution = 0
    for value in distribution:
        sum_distribution += value
        
    return sum_distribution / len(distribution)

function_mean = mean(houses['SalePrice'])
pandas_mean = houses['SalePrice'].mean()

means_are_equal = (function_mean == pandas_mean)

## 8. Estimating the Population Mean ##

parameter = houses['SalePrice'].mean()

sample_size = 5
sampling_errors = []
sample_sizes = []

for i in range(101):
    Sample = houses['SalePrice'].sample(sample_size, random_state = i)
    statistic = Sample.mean()
    sampling_error = parameter - statistic
    sampling_errors.append(sampling_error)
    sample_sizes.append(sample_size)
    sample_size += 29
    
import matplotlib.pyplot as plt
plt.scatter(x = sample_sizes, y = sampling_errors)
plt.axhline(0)
plt.axvline(2930)
plt.xlabel("Sample size")
plt.ylabel("Sampling error")
plt.show()
    
    

## 9. Estimates from Low-Sized Samples ##

means = []

for i in range(10000):
    sample = houses['SalePrice'].sample(100, random_state=i)
    means.append(sample.mean())
    
plt.hist(means)
plt.axvline(houses['SalePrice'].mean())
plt.xlabel('Sample mean')
plt.ylabel('Frequency')
plt.xlim(0,500000)

## 11. The Sample Mean as an Unbiased Estimator ##

population = [3, 7, 2]
population_mean = sum(population) / len(population)
List = []
samples = [[3,7], [7,2], [2,3], [3,2], [7,3], [2,7]]

for sample in samples:
    mean = sum(sample) / len(sample)
    List.append(mean)
    
mean_of_sample_means = sum(List)/len(List) 

unbiased = (mean_of_sample_means == population_mean)