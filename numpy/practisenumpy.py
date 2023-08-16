import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
# sns.set()
# dataFrame = pd.read_csv('/Users/ripeshghimire/coding/python-basics /numpy/numpyfiles/president_heights.csv')
# # print(dataFrame.head())
# #Extracting rows 
# # print(dataFrame.iloc[2])
# #Extracting columns
# # print(dataFrame['height(cm)'])
# #add height in column in numpy array
# height = np.array(dataFrame['height(cm)'])
# # print(height)
# ##Tallest precident
# # print(f'The tallest president height is {np.max(height)}' )
# #Smallest president
# # print(f'The smallest president is height is {np.min(height)}')
# #Average heigh
# mean = np.mean(height)
# # print(f'The average height of the president is {np.mean(height)}')
# #median height
# # print(f'The median height is {np.median(height)}')
# #std
# # print(f'The standard deviation is {np.std(height)}')
# #25 and 75 percentile 
# # print(f'The 25 percentile is {np.percentile(height,25)}')
# # print(f'The 75 percentile is {np.percentile(height,75)}')

# #find number of president whose height is above average 
# avg_above = sum(height>mean)
# print(f'The number of president whose heigh is above average are {avg_above}')
# #find number of president whose heigh is better than 75 of data
# greater = sum(height > np.percentile(height,75))
# print(f'The number of president whose heigh is above 75 are {greater}')
# ##Find number of president whose height is less thant 25% of data
# smaller = sum (height < np.percentile(height,25))
# print(f'The number of president whose heigh is less than 25 are {smaller}')
# ## Find the number of presient whose height is maxium
# maximum_height = sum(height == np.max(height))
# print(f'The number of president with maximum height is  {maximum_height}')

dataFrame = pd.read_csv('/Users/ripeshghimire/coding/python-basics /numpy/numpyfiles/Seattle2014.csv')
pricipitation = np.array(dataFrame['PRCP'])
print(pricipitation)

# no of days with no of rainfall 
# no of days with max rainfall 
# no of days with more than 100mm rainfall
# no of days with 10-100 rainfall
no_rainfall = np.sum(pricipitation == 0)
print(f"The no of days without rainfall is {no_rainfall}")
max_rainfall = np.sum(pricipitation ==np.max(pricipitation))
print(f'The no of max rainfall days is {max_rainfall}')
morethan_100 = np.sum(pricipitation > 100)
print(f'The no of rainfall with more than 100mm rainfall is{morethan_100}')
between10_100 =np.sum((pricipitation<100)&(pricipitation>10))
print(f'The no of rainfalll between 10 and 100 mm is {between10_100}')