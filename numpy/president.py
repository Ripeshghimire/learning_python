import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

# sns.set()
dataFrame = pd.read_csv('numpy/numpyfiles/president_heights.csv')
print(dataFrame.head())
# #Extracting rows 
# # print(dataFrame.iloc[2])
# #Extracting columns
# # print(dataFrame['height(cm)'])
# #add height in column in numpy array
name = np.array(dataFrame['name'])
print(name)
height = np.array(dataFrame['height(cm)'])
# height_name = name[()]
# print(height_name)
# print(max_height) 
# # print(height)
# ##Tallest precident
tallest_president = name[np.argmax(height)]
# print(tallest_president)
plt.plot(height)
plt.show()
print(f'The tallest president is {tallest_president} height is {np.max(height)}' )
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
# plt.hist(height)
# plt.title('heigh distributiion')
# plt.xlabel("Height Cm")
# plt.ylabel("NUMBER")
# plt.show()
plt.savefig('ripesh')