import pandas as pd 
import numpy as np 
user_df = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user',sep = '|' )
print(user_df)
# Step 1. Import the necessary libraries
# Step 2. Import the dataset from this address.
# Step 3. Assign it to a variable called users and use the 'user_id' as index
user_df.set_index('user_id',inplace=True)
# print(user_df)
# Step 4. See the first 25 entries
print(user_df.head(25))
# Step 5. See the last 10 entries
print(user_df.tail(10))
# Step 6. What is the number of observations in the dataset?
no_of_observation = np.prod(user_df.shape)
print(user_df.shape)
print(f'The no of observation is {no_of_observation}')
# Step 7. What is the number of columns in the dataset?
colums = user_df.columns
print(len(colums))
# Step 8. Print the name of all the columns.
print(colums)
# Step 9. How is the dataset indexed?
print (f'The dataset is index this way{user_df.index}')
# Step 10. What is the data type of each column?
print(colums.dtype)
# Step 11. Print only the occupation column
occupation = user_df['occupation'].nunique()
# Step 12. How many different occupations are in this dataset?
occupation = user_df['occupation'].unique()
# Step 13. What is the most frequent occupation?
print(user_df['occupation'].value_counts().head(1).index[0])
# Step 14. Summarize the DataFrame.
print(user_df.describe())
# Step 15. Summarize all the columns
print(user_df.describe(include = 'all'))
# Step 16. Summarize only the occupation column
# Step 17. What is the mean age of users?
age = user_df['age']
print(np.mean(age))
# Step 18. What is the age with least occurrence?f
age =  [] 

