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
# y = x.dropna()
# print(f'Y values ==== \n{y}')
# print(f'x values ==== \n {x}')

# y = x.dropna(inplace=True)
# print(f'Y values ==== \n{y}')
# print(f'x values ==== \n {x}')


df = pd.DataFrame([[1,np.nan,2],
                   [2,3,5],
                   [np.nan,4,6]])
# print(df)
# drops columns having null values 
# y = df.dropna(axis='columns')


# drop rows having null values 
# df.dropna(axis='rows')

df[3] = np.nan
# 
# ae = df.dropna(axis="columns",how= 'any')
# print(ae)
# # 
# az = df.dropna(axis="columns",how="all")
# print(az)
# # 
# ag = df.dropna(axis="columns",thresh=2)
# print(ag)

#  using fill na 
ae = df.fillna(axis="columns",value= 12)
print(ae)