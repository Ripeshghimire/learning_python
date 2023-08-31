import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

df  = pd.read_csv('numpy/numpyfiles/Building_Permits.csv',low_memory= False)
# print(df.head())
# print(df.columns)
# print(df.info)
dataShape = df.shape
print(dataShape)

totalCelss = np.prod(dataShape)
print(f'Total cells is {totalCelss}')

missingDataPerColumn = np.sum(df.isnull())
# print(missingDataPerColumn)
total_missing_data  = np.sum(missingDataPerColumn)
# print(total_missing_data)
missing_percentage = total_missing_data / totalCelss * 100 
print(missing_percentage)
# use similar analysis for street no suffix and zip code 
suffix = df['Street Number Suffix']
zipcode = df['Zipcode']
total_rows = 198900
missingDatainZipcode = np.sum(zipcode.isnull())
percentagezipcode = missingDatainZipcode / total_rows * 100
missingDataInSuffix = np.sum(suffix.isnull())
percentagesuffix = missingDataInSuffix/ total_rows * 100
print(percentagesuffix)
print(percentagezipcode)
