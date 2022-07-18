## 3. Populations and Samples ##

question1 = 'population'
question2 = 'population'
question3 = 'sample'
question4 = 'population'
question5 = 'sample'

## 4. Sampling Error ##

import pandas as pd
wnba = pd.read_csv('wnba.csv')

wnba.head()
wnba.tail()

wnba.shape

parameter = wnba['Games Played'].max()
sample = wnba.sample(30, random_state = 1)

statistic = sample['Games Played'].max()

sampling_error = parameter - statistic

## 5. Simple Random Sampling ##

import pandas as pd
import matplotlib.pyplot as plt

wnba = pd.read_csv('wnba.csv')

L = []
Mean = wnba['PTS'].mean()
for i in range(100):
    pts = wnba['PTS'].sample(10, random_state = i)
    mean = pts.mean()
    L.append(mean)
    
plt.scatter(range(1, 101), L)
plt.axhline(Mean)
plt.show()

## 7. Stratified Sampling ##

wnba['Pts_per_game'] = wnba['PTS']/wnba['Games Played']

stratum_G = wnba[wnba['Pos'] == 'G']
stratum_F = wnba[wnba['Pos'] == 'F']
stratum_C = wnba[wnba['Pos'] == 'C']
stratum_FC = wnba[wnba['Pos'] == 'F/C']
stratum_GF = wnba[wnba['Pos'] == 'G/F']

points_per_position = {}
for stratum, position in [(stratum_G, 'G'), (stratum_F, 'F'), (stratum_C, 'C'), (stratum_GF, 'G/F'), (stratum_FC, 'F/C')]:
    sample = stratum['Pts_per_game'].sample(10, random_state = 0)
    points_per_position[position] = sample.mean()

k = points_per_position.keys()
v = points_per_position.values()

position_most_points = 'C'


    
    

## 8. Proportional Stratified Sampling ##

under_12 = wnba[ wnba['Games Played'] <= 12]
btw_13_22 = wnba[(wnba['Games Played'] > 12) & (wnba['Games Played'] <= 22)]
over_23  = wnba[ wnba['Games Played'] > 22]

mean_list = []
population_mean = wnba['PTS'].mean()
for i in range(100):
    sample_under_12 = under_12.sample(1, random_state = i)
    sample_btw_13_22 = btw_13_22.sample(2, random_state = i)
    sample_over_23 = over_23.sample(7, random_state = i)
    sample = pd.concat([sample_under_12, sample_btw_13_22, sample_over_23])
    
    mean = sample['PTS'].mean()
    mean_list.append(mean)

plt.scatter(range(1, 101), mean_list)
plt.axhline(population_mean)

## 10. Cluster Sampling ##

clusters = pd.Series(wnba['Team'].unique()).sample(4, random_state = 0)

sample = pd.DataFrame()

for cluster in clusters:
    data_collected = wnba[wnba['Team'] == cluster]
    sample = sample.append(data_collected)
    
Height = sample['Height'].mean()
Age = sample['Age'].mean()
BMI = sample['BMI'].mean()
PTS = sample['PTS'].mean()

sampling_error_height = (wnba['Height'].mean())-Height
sampling_error_age = (wnba['Age'].mean())-Age
sampling_error_BMI = (wnba['BMI'].mean())-BMI
sampling_error_points = (wnba['PTS'].mean()-PTS)