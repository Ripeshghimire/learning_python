data = [
    {'price':85000,'rooms':4,'neighborhood':'Jawalakhel'},
    {'price':70000,'rooms':3,'neighborhood':'Kopundole'},
    {'price':65000,'rooms':3,'neighborhood':'Kapan'},
    {'price':60000,'rooms':2,'neighborhood':'Kopundole'},
]
newData  = {'Jawalakhel':1,'Kupondole':2,'Kapan':1}

import numpy as np 
from sklearn.feature_extraction import DictVectorizer
vec = DictVectorizer(sparse=False,dtype=int)
newData = vec.fit_transform(data)
print(vec.get_feature_names_out())
print()