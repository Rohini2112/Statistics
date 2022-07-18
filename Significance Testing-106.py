## 3. Statistical Significance ##

import numpy as np
import matplotlib.pyplot as plt

mean_group_a = np.mean(weight_lost_a)
mean_group_b = np.mean(weight_lost_b)

## 4. Test Statistic ##

import numpy as np
import matplotlib.pyplot as plt

mean_group_a = np.mean(weight_lost_a)
mean_group_b = np.mean(weight_lost_b)

mean_difference = mean_group_b - mean_group_a

## 5. Permutation Test ##

mean_difference = 2.52
print(all_values)

mean_differences = []
for i in range(1000):
    group_a = []
    group_b = []
    for val in all_values:
        value = numpy.random.rand()
        if value >= 0.5:
            group_a.append(val)
        else:
            group_b.append(val)
        
    mean_a = numpy.mean(group_a)
    mean_b = numpy.mean(group_b)
    iteration_mean_difference = mean_b - mean_a
    mean_differences.append(iteration_mean_difference)

plt.hist(mean_differences)
plt.show()
        
    

## 7. Dictionary Representation of a Distribution ##

sampling_distribution = {}

for key in mean_differences:
    if sampling_distribution.get(key, False):
        val = sampling_distribution.get(key)
        val = val + 1
        sampling_distribution[key] = val
    else:
        sampling_distribution[key] = 1

## 8. P Value ##

frequencies = []
for key in sampling_distribution.keys():
    if key >= 2.52:
         frequencies.append(sampling_distribution[key])
        
total = numpy.sum(frequencies)
p_value = total/1000