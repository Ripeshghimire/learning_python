import numpy as np
import seaborn as sns
sns.set()
iris_data = sns.load_dataset('iris')
# extraction of only the feature set
X_iris = iris_data.drop(columns='species')
# extraction of target set
y_iris = iris_data['species']

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=10)
model.fit(X_iris, y_iris)
y_pred = model.predict(X_iris)

from sklearn.metrics import accuracy_score
accuray  = accuracy_score(y_pred,y_iris)
print(f'The accuracy score is {accuray * 100}')

print("After using model holdout ")
from sklearn.model_selection import train_test_split
x_train, X_test, y_train, y_test = train_test_split(X_iris, y_iris, train_size=0.5, random_state=101, shuffle=True)
model.fit(x_train, y_train)
y_pred2 = model.predict(X_test)

accuracy2 = accuracy_score(y_pred2,y_test)


# cross validation
from sklearn.model_selection import cross_val_score
cvScore = cross_val_score(model,X_iris,y_iris,cv=5)
print("CV score ",np.mean(cvScore))