import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt


# Given are two data sets for different house prices in Kathmandu and Lalitpur. 
# ●	Visualize the data and explain your findings in the two different cities
# plt.hist(heights)
# plt.xlabel("height(cm)")
# plt.ylabel("no")
# plt.show()
kathmandu = pd.read_csv('numpy/numpyfiles/KathmanduHouse_1.csv')
lalitpur = pd.read_csv('numpy/numpyfiles/LalitpurHouuse.csv')
# print(lalitpur)
price_kathmandu  = np.array(kathmandu['Price'])
price_lalitpur = np.array(lalitpur['price'])
# print(price_kathmandu)
# print(price_lalitpur)

# ●	What is the least amount of money that I should have to buy a house in Kathmandu ?
least_house_price_ktm = np.min(price_kathmandu)
print(f'The least amount of money that i should have to buy a house in kathnmandu is {least_house_price_ktm}')
# ●	What is the least amount of money that I should have to buy a house in Lalitpur ?
least_house_price_ltr = np.min(price_lalitpur)
print(f'The least amount of money that i should have to buy a house in ktm is {least_house_price_ltr}')
# ●	How much money should I have to buy the most expensive house in Kathmandu ?
expensive_ktm = np.max(price_kathmandu)
print(f'The maximum amount of money i should have to buy a expensive house is {expensive_ktm}')
# ●	How much money should I have to buy the most expensive house in Lalitpur ?
expensive_ltr  = np.max(price_lalitpur)
print(f'The maximum amount of money i should have to buy a expensince house in lalitpur is {expensive_ltr}')
# ●	Where is it cheap to buy 50% of the houses?
ktm_median = np.median(price_kathmandu)
ltr_median = np.median(price_lalitpur)
if ktm_median > ltr_median:
    print(f'laltipur house are cheap to buy in the 50% {ltr_median}')
else:
     print(f'ktm house are cheap to buy in the 50% {ktm_median}')
# ●	In which district will I have more price choices?
unique = np.unique(price_kathmandu)
unique2  = np.unique(price_lalitpur)
ktm = (np.size(unique))
ltr = (np.size(unique2))
print(f'ktm will have the most choices of price {ktm}')
# ●	What the price range of min 25 % of the houses and maximmum 25% of the houses 
min_kathmandu = np.percentile(price_kathmandu,25)
max_kathmandu = np.percentile(price_kathmandu,75)
min_lalitpur= np.percentile(price_lalitpur,25)
max_lalitpur= np.percentile(price_lalitpur,75)
print(f'the price range of ktm is {min_kathmandu} to {max_kathmandu}')
print(f'The price range of ltr is {min_lalitpur} to {max_lalitpur}')

