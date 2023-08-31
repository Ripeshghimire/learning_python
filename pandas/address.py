import numpy as np 
import pandas as pd 
euro12 = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv')
# print(df.head())Step 1. Import the necessary libraries
# Step 2. Import the dataset from this address.
# Step 3. Assign it to a variable called euro12.
# Step 4. Select only the Goal column.
goal = euro12['Goals']
print(goal)
# Step 5. How many team participated in the Euro2012?
print(len(euro12['Team']))
# Step 6. What is the number of columns in the dataset?
print(len(euro12.columns))
# Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
team1  = ['Team','Yellow Cards','Red Cards']
disciplie = euro12[team1]
# print(disciplie)
# Step 8. Sort the teams by Red Cards, then to Yellow Cards

yellow = disciplie.sort_values(by=['Red Cards','Yellow Cards'],ascending=False)
print(yellow)
# Step 9. Calculate the mean Yellow Cards given per Team
mean_yellow = np.mean(disciplie['Yellow Cards'])
print(mean_yellow)
team = euro12['Team']
# Step 10. Filter teams that scored more than 6 goals
print(euro12[euro12['Goals']>6])
# Step 11. Select the teams that start with G
# team = disciplie['Team']
# for team in team:
#     if team == team[team.find('G'):]:
        # print(team)
# Step 12. Select the first 7 columns
print(euro12.iloc[:,:7])
# Step 13. Select all columns except the last 3
print(euro12.iloc[:,:-3])
# Step 14. Present only the Shooting Accuracy from England, Italy and Russia
# shooting = euro12['Shooting Accuracy']
# new_list = ['England', 'Italy', 'Russia']
print("Shooting accuracy form england, russia and italy")
myData = euro12['Team'].isin(['England', 'Italy', 'Russia'])
print(myData)
shootingAccuracyAndTeam = euro12.loc[euro12['Team'].isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']]
print(shootingAccuracyAndTeam)