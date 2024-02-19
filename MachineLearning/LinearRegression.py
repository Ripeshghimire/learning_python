import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
df = pd.read_csv('headbrain.csv')
print(df.drop(columns=['Gender','Age Range',],inplace=True))
# print(df.head()
X = df['Head Size(cm^3)']
X = X[:, np.newaxis]
y = df['Brain Weight(grams)']
model = LinearRegression(fit_intercept= True)
model.fit(X, y)
model.predict(X)
plt.scatter(X, y)
plt.plot(X, y)
plt.show()

