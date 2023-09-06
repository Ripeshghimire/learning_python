import pandas as pd
import numpy as np
# Target set nsamples --- one dimension array ---what we want to predict
# Feature set == nsamples , nfeatures -- multidimensional array -- rest of the data other than the data set
# Extraction of data
dataFrame  = pd.read_csv('Iris.csv')
print(dataFrame.head())
print('------------')
# Target Set = small y
y = dataFrame['Species']
print(y)
print(y.shape)

print("feature Set ")
X = dataFrame.drop(columns=['Species'])
print(X)
print(X.shape)