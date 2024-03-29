## 2. Calculating Differences ##

female_diff = (10771-16280.5)/16280.5
male_diff = (21790-16280.5)/16280.5

## 3. Updating the Formula ##

female_diff = ((10771-16280.5)**2)/16280.5
male_diff = ((21790-16280.5)**2)/16280.5

gender_chisq = female_diff + male_diff

## 4. Generating a Distribution ##

chi_squared_values = []
from numpy.random import random
import matplotlib.pyplot as plt

for val in range(1000):
    vector = random((32561,))
    vector[vector < 0.5] = 0
    vector[vector >= 0.5] = 1
    male_count = len(vector[vector == 0])
    female_count = len(vector[vector == 1])
    male_diff = ((male_count - 16280.5)**2)/16280.5
    female_diff = ((female_count - 16280.5)**2)/16280.5
    chi_squared = male_diff + female_diff
    chi_squared_values.append(chi_squared)
    
plt.hist(chi_squared_values)

## 6. Smaller Samples ##

female_diff = (107.71-162.805)**2 / 162.805
male_diff = (217.90-162.805)**2 / 162.805

gender_chisq = female_diff + male_diff

## 7. Sampling Distribution Equality ##

chi_squared_values = []
from numpy.random import random
import matplotlib.pyplot as plt

for val in range(1000):
    sequence = random((300,))
    sequence[sequence < 0.5] = 0
    sequence[sequence >= 0.5] = 1
    female_count = len(sequence[sequence == 1])
    male_count = len(sequence[sequence == 0])
    female_diff = (female_count - 150)**2 / 150
    male_diff = (male_count - 150)**2 / 150
    chi_squared = female_diff + male_diff
    chi_squared_values.append(chi_squared)
    
plt.hist(chi_squared_values)

## 9. Increasing Degrees of Freedom ##

import pandas as pd
income = pd.read_csv('income.csv')

diffs = []
observed = [27816, 3124, 1039, 311, 271]
expected = [26146.5, 3939.9, 944.3, 260.5, 1269.8]
    
for i, obs in enumerate(observed):
    exp = expected[i]
    diff = (obs - exp)**2 / exp
    diffs.append(diff)

race_chisq = sum(diffs)

## 10. Using SciPy ##

from scipy.stats import chisquare
import numpy as np

observed = np.array([27816, 3124, 1039, 311, 271])
expected = np.array([26146.5, 3939.9, 944.3, 260.5, 1269.8])

chisquare_value, race_pvalue = chisquare(observed, expected)