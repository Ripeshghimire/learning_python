import numpy as np 
import pandas as pd 
dataFrame = pd.read_csv('numpy/numpyfiles/Iris.csv')
sepallength = np.array(dataFrame['SepalLengthCm'])
sepalwidth = np.array(dataFrame['SepalWidthCm'])
petallength  = np.array(dataFrame['PetalLengthCm'])
petalwidth = np.array(dataFrame['PetalWidthCm'])
species = np.array(dataFrame['Species'])
# Flower whose petal_length is greater than 4 is a large flower, less than 2 is small and
# between 2 and 4 is medium flower
greaterthan_four = petallength > 4
medium_flower = (petallength > 2) & (petallength<=4)
small_flower = petallength <= 2
# Find the total number of large, small and medium flower
print(f'The total number of large flower is {np.sum(greaterthan_four)}')
print(f'The total number of mediun flower is {np.sum(medium_flower)}')
print(f'The total number of small flower is {np.sum(small_flower)}')
# average sepal length ,sepal_width ,petal length,petal_width
print(f'The average sepal lenght is {np.mean(sepallength)}')
print(f'The average sepal width is {np.mean(sepalwidth)}')
print(f'The average petal length is {np.mean(petallength)}')
print(f'The average petal widht is {np.mean(petalwidth)}')
# max sepal length ,sepal_width ,petal length,petal_width
print(f'The max sepal lenght is {np.max(sepallength)}')
print(f'The max sepal width is {np.max(sepalwidth)}')
print(f'The max petal length is {np.max(petallength)}')
print(f'The max petal widht is {np.max(petalwidth)}')
# In this data set which is the most occurred species and which is the least occurred.
uniquespeices = np.unique(species)
print(uniquespeices)
setosa = species == uniquespeices[0]
print(sum(setosa))
versicolor = species == uniquespeices[1]
print(sum(versicolor))
virginica = species == uniquespeices[2]
print(sum(virginica))
