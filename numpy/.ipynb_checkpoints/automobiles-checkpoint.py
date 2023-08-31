import numpy as np 
import pandas as pd 
df = pd.read_csv('numpy/numpyfiles/automobile.csv')
price = np.array(df['price'])
car_name = np.array(df['make'])
print(car_name)
# print(price)
#highest price car 
highest_price_index = np.argmax(price)
# highest_price_car = price[highest_price_index]
# name  = car_name[highest_price_car]
# print(f'The highest price car is {name} and its price is {highest_price_car}')