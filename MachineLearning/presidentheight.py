import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
training_set = pd.read_csv('president_heights.csv')
print(training_set.head())
height = training_set['height(cm)']

