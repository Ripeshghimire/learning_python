import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


def PolynomialRegression(degree=2, **kwargs):
    return make_pipeline(PolynomialFeatures(degree), LinearRegression(**kwargs))

def make_data(N, rseed=1):
    rng = np.random.RandomState(rseed)
    ###rand(rows=N,colums = 1)
    X = rng.rand(N, 1) ** 2
    y = 10 - 1 / (X.ravel() + 0.1)
    return X, y

Xtrain, ytrain = make_data(40)

##visulize the data using plot

plt.scatter(Xtrain.ravel(), ytrain, c='black')
axis = plt.axis()


# Creation for test data
X_test = np.linspace(-0.1, 1.1, 500)[:, np.newaxis]


degress = [1, 3, 5,30]

for degree in degress:
    yPred = PolynomialRegression(degree).fit(Xtrain, ytrain).predict(X_test)
    plt.plot(X_test.ravel(), yPred, label=f'degree {degree}')
plt.xlim(-0.1,1.0)
plt.ylim(-2,12)
plt.legend(loc='best')
plt.show()
#Validation Curve
print("Valdation Score")
from sklearn.model_selection import validation_curve
degree = np.arange(0,70)
train_score, val_score = validation_curve(estimator=PolynomialRegression(), X=Xtrain, y=ytrain,param_name='polynomialfeatures__degree',param_range=degree,cv=7)
print(train_score)
print(val_score)
plt.plot(degree,np.median(train_score,1),color='blue',label='Training Score')
plt.plot(degree,np.median(val_score,1),color='red',label='Validation Score')
plt.legend(loc='best')
plt.ylim(0,1.2)
plt.xlabel('degree')
plt.ylabel('score')
plt.show()


###Checking for data
Xtrain2, ytrain2 = make_data(1000)
plt.scatter(Xtrain2.ravel(),ytrain2)
axis = plt.axis()
plt.show()

degree = np.arange(0,100)
train_score2, val_score2 = validation_curve(estimator=PolynomialRegression(), X=Xtrain2, y=ytrain2,param_name='polynomialfeatures__degree',param_range=degree,cv=7)
plt.plot(degree,np.median(train_score2,1),color='blue',label='Training Score',linestyle='dashed')
plt.plot(degree,np.median(val_score2,1),color='red',label='Validation Score',linestyle='dashed')
plt.legend(loc='best')
plt.ylim(0,1.2)
plt.xlabel('degree')
plt.ylabel('score')
plt.show()