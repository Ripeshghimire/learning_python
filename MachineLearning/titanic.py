import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
sns.set()
titanic = sns.load_dataset('titanic')
print(titanic.head(5))
print(titanic.columns)
print(titanic['adult_male'])