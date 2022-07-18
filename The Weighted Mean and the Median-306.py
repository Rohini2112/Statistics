## 1. Introduction ##

mean_new = houses_per_year['Mean Price'].mean()
mean_original = houses['SalePrice'].mean()
difference = mean_original - mean_new

## 2. Different Weights ##

houses_per_year['sum_per_year'] = houses_per_year['Mean Price']*houses_per_year['Houses Sold']
all_sums_together = houses_per_year['sum_per_year'].sum()
total_n_houses = houses_per_year['Houses Sold'].sum()
weighted_mean = round((all_sums_together / total_n_houses), 10)

mean_original = round(houses['SalePrice'].mean(), 10)

difference = mean_original - weighted_mean

## 3. The Weighted Mean ##

def weighted_mean_func(distribution_1, distribution_2):
    total = sum(distribution_1*distribution_2)
    weight = sum(distribution_2)
    weighted_mean = total / weight
    return weighted_mean

weighted_mean_function = weighted_mean_func(houses_per_year['Mean Price'], houses_per_year['Houses Sold'])
weighted_mean_function = round(weighted_mean_function, 10)
weighted_mean_numpy = round(numpy.average(houses_per_year['Mean Price'], weights = houses_per_year['Houses Sold']), 10)
    
equal = weighted_mean_function == weighted_mean_numpy    
    

## 4. The Median for Open-ended Distributions ##

distribution1 = [23, 24, 22, '20 years or lower,', 23, 42, 35]
distribution2 = [55, 38, 123, 40, 71]
distribution3 = [45, 22, 7, '5 books or lower', 32, 65, '100 books or more']

median1 = 23
median2 = 55
median3 = 32

## 5. Distributions with Even Number of Values ##

rooms = houses['TotRms AbvGrd'].copy()
rooms = rooms.replace({'10 or more': 10})
rooms = rooms.astype(int)
rooms_sorted = rooms.sort_values()

middle_indices = [int((len(rooms_sorted) / 2) - 1),
                  int((len(rooms_sorted) / 2))]
middle_values = rooms_sorted.iloc[middle_indices]
median = middle_values.mean()

## 6. The Median as a Resistant Statistic ##

plt.boxplot(houses['Lot Area'])
plt.show()
houses['SalePrice'].plot.box()
plt.show()

Lot_area_mean = houses['Lot Area'].mean()
Lot_area_median = houses['Lot Area'].median()
SalePrice_mean = houses['SalePrice'].mean()
SalePrice_median = houses['SalePrice'].median()

lotarea_difference = Lot_area_mean - Lot_area_median
saleprice_difference = SalePrice_mean - SalePrice_median

## 7. The Median for Ordinal Scales ##

mean = houses['Overall Cond'].mean()
median = houses['Overall Cond'].median()

plt.hist(houses['Overall Cond'])
plt.show()

more_representative = 'mean'