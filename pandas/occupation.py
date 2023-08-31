import numpy as np 
import pandas as pd 
df = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user',sep='|')
print(df.head())
print(df.columns)
# Step 4. Discover what is the mean age per occupation
mean_age_per_occupation = df.groupby('occupation')['age'].mean()
print("Mean Age per Occupation:")
print(mean_age_per_occupation)
# Step 5. Discover the Male ratio per occupation and sort it from the most to the least
male_ratio_per_occupation = df.groupby('occupation')['gender'].apply(lambda x: (x == 'M').sum() / x.count())
sorted_male_ratio = male_ratio_per_occupation.sort_values(ascending=False)
print("Male Ratio per Occupation (Sorted):")
print(sorted_male_ratio)
# Step 6. For each occupation, calculate the minimum and maximum ages

# Step 7. For each combination of occupation and gender, calculate the mean age

# Step 8. For each occupation present the percentage of women and men
