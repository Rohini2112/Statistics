## 2. Calculating Expected Values ##

males_over50k = 0.67*0.241*32561
males_under50k = 0.67*0.759*32561
females_over50k = 0.33*0.241*32561
females_under50k = 0.33*0.759*32561

## 3. Calculating Chi-squared ##

observed = [6662, 1179, 15128, 9592]
expected = [5257.6, 2589.6, 16558.2, 8155.6]
values = []

for i, obs in enumerate(observed):
    exp = expected[i]
    value = (obs - exp) ** 2 / exp
    values.append(value)

chisq_gender_income = sum(values)

## 4. Finding statistical significance ##

import numpy as np
from scipy.stats import chisquare

observed = np.array([6662, 1179, 15128, 9592])
expected = np.array([5257.6, 2589.6, 16558.2, 8155.6])
chisq_value, pvalue_gender_income = chisquare(observed, expected)

## 5. Cross Tables ##

import pandas as pd

table = pd.crosstab(income['sex'], income['race'])
print(table)

## 6. Finding Expected Values ##

import numpy as np 
from scipy.stats import chi2_contingency
table = pd.crosstab(income['sex'], income['race'])
chisq_value, pvalue_gender_race, df, expected = chi2_contingency(table)