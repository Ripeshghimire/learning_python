# • Basics of the API Most commonly, the steps in using the Scikit-Learn estimator API are as follows
# • 1. Choose a class of model by importing the appropriate estimator class from
# ScikitLearn.
# • 2. Choose model hyper parameters by instantiating this class with desired values.
# • 3. Arrange data into a features matrix and target vector following the discussion from before.
# • 4. Fit the model to your data by calling the fit) method of the model instance.
# • 5. Apply the model to new data:
# • For supervised learning, often we predict labels for unknown data using the predict() method.
# • For unsupervised learning, we often transform or infer properties of the data using the transform() or predict() method.
import random
import numpy as np
import matplotlib.pyplot as plt
#Creating a random data
rng = np.random.RandomState(42)
x = 10 * rng.rand(50)
print("X Dataaaaa")
print(x.shape)

# generating y
y = 2 * (x-1) + rng.rand(50)
##Visulaizing data
# plt.scatter(x,y)
# plt.xlabel('X DATA')
# plt.ylabel('Y Data')
# plt.show()

# • 1. Choose a class of model by importing the appropriate estimator class from
# ScikitLearn.
from sklearn.linear_model import LinearRegression

#   Choose model hyper parameters by instantiating this class with desired values.
model = LinearRegression(fit_intercept= True)

# 3. Arrange data into a features matrix and target vector following the discussion from before.
# X  = nsamples,nfeatures
# y - nsamples
print('After new dimension')
X = x[:,np.newaxis]
print(X.shape)
# FIT THE MODEL TO YOUR DATA
model.fit(X,y)
# Getting result of the model
print("Result==============")
# coeff =
#COefff == slope of data gives the relation between two X and y, if x is +ve then
#When x increases y increses and negative vice versa
#The more the slope the more the relation
print(model.coef_)
#Gives the predicted value of Y when X is 0
print(model.intercept_)


##PREDICTING
xfit = np.linspace(-1,11)

#Changing to nsample, nfeature
Xfit = xfit[:,np.newaxis]
yfit = model.predict(Xfit)

print("Predicted Data")
print(yfit)

##Seeing and interpreting result
plt.scatter(x,y,c='red')
plt.plot(xfit,yfit)
plt.show()