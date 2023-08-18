import numpy as np 
import pandas as pd 
# -------------------------------------------SEATTLE----------------------------------
dataFrame = pd.read_csv('/Users/ripeshghimire/coding/python/numpy/numpyfiles/Seattle2014.csv')
pricipitation = np.array(dataFrame['PRCP'])
# print(pricipitation)

# no of days with no of rainfall 
# no of days with max rainfall 
# no of days with more than 100mm rainfall
# no of days with 10-100 rainfall
no_rainfall = np.sum(pricipitation == 0)
# print(f"The no of days without rainfall is {no_rainfall}")
# max_rainfall = np.sum(pricipitation ==np.max(pricipitation))
# print(f'The no of max rainfall days is {max_rainfall}')
morethan_100 = np.sum(pricipitation > 100)
# print(f'The no of rainfall with more than 100mm rainfall is{morethan_100}')
between10_100 =np.sum((pricipitation<100)&(pricipitation>10))
# print(f'The no of rainfalll between 10 and 100 mm is {between10_100}') 
#find only rainy days 
rainy_days = pricipitation[pricipitation > 0]
days = np.arange(365)
summer_days = pricipitation[(days > 173) & (days <273)]
print(summer_days)
no_summerday = pricipitation[days != summer_days]
print(f'The rainy days are {rainy_days}')
# median rainfall on rainy days
print(f'The median rainfall on rainy days is {np.median(rainy_days)}')
# maximum rainfall on rainy days 
print(f'The maximun rainfall on rainy days is {np.max(rainy_days)}')
#median rainfall on summer days 
print(f'The rainfall on summer days is {np.median(summer_days)}')
# min rainfall on summer days
print(f'The min rainfall on summer days is {np.min(summer_days)}')
# min rainfall on no summer day
print(f'The min rainfall on no summer days is{np.min(no_summerday)}')

