import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from collections import counter 
chipo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv',sep ='\t')
# print(chipo)
# # Step 4. See the first 10 entries
# print(chipo.head())
# # Step 5. What is the number of observations in the dataset?
# print(chipo.shape[0])
# print(chipo.shape[1])
# # Step 6. What is the number of columns in the dataset?
# print (len(chipo.columns))
# # Step 7. Print the name of all the columns.
# print(chipo.columns)
# # Step 8. How is the dataset indexed?
# print(chipo.index)
# # Step 9. Which was the most-ordered item?
# item = chipo['item_name']
# print(item[chipo['quantity'].value_counts().head(1)])
# # Step 10. For the most-ordered item, how many items were ordered?
# print(chipo['quantity'].value_counts().head(1).index)
# # Step 11. What was the most ordered item in the choice_description column?
# choice_descriptiion = chipo['choice_description']
# print(choice_descriptiion[chipo['quantity'].value_counts().head(1)])
# groupItem = chipo.groupby('choice_description').sum()
# groupItem = groupItem.sort_values(by ='quantity',ascending=True)

# print(groupItem.head(1))
# # Step 12. How many items were orderd in total?
# # print(np.sum(chipo['quantity']))
# # Step 13. Turn the item price into a float
# item_price = chipo['item_price']
# # item_price = item_price.astype('float').str.replace('$', '')
# # Step 13.a. Check the item price type
# print(item_price.dtype)
# Step 13.b. Create a lambda function and change the type of item pricef

# Step 13.c. Check the item price type

# Step 14. How much was the revenue for the period in the dataset?

# Step 15. How many orders were made in the period?
# print(chipo['order'])                        
# Step 16. What is the average revenue amount per order?
# Step 17. How many different items are sold?

# create a histogram for top 5 items bought
#Change it to datafraome ## passing orient to index to
item_name = chipo['item_name']
counts = Counter(item_name)
df = pd.DataFrame.from_dict (counts, orient="index")
print ('Data Frame')
print(df)
print(df .columns)
print("Data Fromsss Sorted Data")
sortedData = df [0].sort_values (ascending=False)
print (sortedData.head (6))
sortedDataFive = sortedData[:6]
print ("Sorted Firve Itenssssssss")
print (sortedDataFive)
sortedDataFive.plot(kind='bar')
plt.xlabel ('Items')
plt.ylabel ("No ordered")
plt.title('TOP 5 ITEMS')
plt.show()