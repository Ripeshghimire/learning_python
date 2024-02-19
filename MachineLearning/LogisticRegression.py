import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
from sklearn.linear_model import LogisticRegression
sns.set()
titanic = pd.read_csv('titanic.csv')
print(titanic.head())
print(titanic.columns)

print("Number of passenger", titanic.shape[0])
print(np.sum(titanic.isnull()))

print("Analysing Data")
# sns.countplot(x='Survived', data=titanic)
# plt.show()
# classify as gender
# sns.countplot(x='Survived', hue='Sex', data=titanic)
# plt.show()
# sns.countplot(x='Survived', hue='Pclass', data=titanic)
# plt.show()
# sns.countplot(x='Survived', hue='Embarked', data=titanic)
# plt.show()
print("removing cabin")
titanic.drop(columns='Cabin', axis=1, inplace= True)
print(np.sum(titanic.isnull()))
print("removing data null values")
titanic.dropna(axis=0, inplace=True)
print(np.sum(titanic.isnull()))
print(titanic['Embarked'])

# changing categorical value
sex = pd.get_dummies(titanic['Sex'], drop_first=True)
print(sex)

# changing catergorical value of enmbarked and plcass
print("embarked========")
embarked = pd.get_dummies(titanic['Embarked'], drop_first=True )
print(embarked)

print("Pclassssss ======== ")
p_class = pd.get_dummies(titanic['Pclass'], drop_first=True)
print(p_class)

titanic = pd.concat([titanic, p_class, embarked, sex],axis=1)
print(titanic.head().to_string())

titanic.drop(columns=['Pclass', 'Sex', 'Embarked', 'PassengerId', 'Name', 'Ticket'],inplace=True)
print(titanic.head())
print(titanic.dtypes)
from sklearn.model_selection import train_test_split
X = titanic.drop(columns='Survived')
y = titanic['Survived']
X.columns = X.columns.astype(str)
trainX,testX,yTrain,yTest = train_test_split(X,y,random_state=1,train_size=0.5)
model = LogisticRegression()
model.fit(trainX,yTrain)
predY = model.predict(testX)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(predY,yTest)
print(accuracy)
print(titanic.dtypes)

from sklearn.metrics import confusion_matrix
cf = confusion_matrix(yTest,predY)
sns.heatmap(cf)