import numpy as np 
import pandas as pd 
x = pd.Series([1,2,3,None,np.nan])
# print(x)
# # check if null values
# print(x.isnull())
# # checking no of null values 
# print(x.isnull())
# # find the null values 
# print(x[x.isnull()])

# # checking not null 
# print(x.notnull())
# print(x[x.notnull()])


# cleaning values 
y = x.dropna()
# print(f'Y values ==== \n{y}')
# print(f'x values ==== \n {x}')

y = x.dropna(inplace=True)
print(f'Y values ==== \n{y}')
print(f'x values ==== \n {x}')