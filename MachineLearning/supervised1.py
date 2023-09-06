import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import seaborn as sns
sns.set()
# Getting the data
iris_data = sns.load_dataset('iris')
# print(iris_data.sample(10))
# getting the iris data
y_iris = iris_data['species']
X_iris = iris_data.drop(columns=['species'])

# splitting the data
from sklearn.model_selection import train_test_split
xtrain,x_test,y_train,y_test = train_test_split(X_iris,y_iris,random_state=23,train_size=0.5)
# Gausion naive bayers
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(xtrain,y_train)
yPred = model.predict(x_test)
print(yPred)
# accuracy
from sklearn.metrics import  accuracy_score
score = accuracy_score(y_test,yPred)
print(f'The accuracy is {score * 100 }')


