import pandas as pd 
import numpy as np
#use of pandas 
#data cleaning 
#data formatting 
# mySeries = pd.Series([1,2,3,'ripesh',1.0,True,])
# print(mySeries)

# #Acessing a value 
# print(mySeries[4])
# # print values only
# print(mySeries.values)
# #index only
# print(mySeries.index)

# #-------------------------------------------------------------
# print("Explicit indexing-------p---------")
# myNewSeries = pd.Series([1,2,3,4,5,6],index=['a','b','c','b','e','f'])
# inde = myNewSeries['b']
# print(myNewSeries)


# studentMarks  = pd.Series([100,20,35,98,23])
# studentRoll = pd.Series([44,42,43,101,12])
# studentMarks.index = studentRoll
# print(studentRoll.is_unique)
# print(studentMarks.index)
# print(studentMarks[44])
# print(studentMarks[101])

# #pandas dataFrame 
# date_of_birth = {
# 'Ripesh':'August 21',
# 'Dikshya':'September 6 ',
# 'Ram':'July 1 ',
# 'Shyam':'September 21'
# }
# mySeries = pd.Series(date_of_birth)
# print(mySeries)
# print(mySeries.index)
# print(mySeries.values)

# print(mySeries['Ripesh'])
#creating dataFrame from dictionary
# dataFrame = pd.DataFrame([{'a':23,'b':24},{'c':12,'d':54},{'e':34,'f':312}])
# print(dataFrame)
area_dict = {'California': 423967,
             'Texas': 695662,
             'New York': 141297,
             'Florida': 170312,
             'Illinois': 149995
             }

population_dict = {'California': 3833251,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135
                   }
areaSeries = pd.Series(area_dict)
populationSeries = pd.Series(population_dict)
# print(areaSeries)
statesDataFrame = pd.DataFrame({'population':populationSeries,'Area':areaSeries})
print(statesDataFrame)
print(statesDataFrame.head())
statesDataFrame['density'] = statesDataFrame['population'] / statesDataFrame['Area']
print(statesDataFrame)
print(statesDataFrame.iloc[:3,:2])
print(statesDataFrame.loc[:3,:2])

# data = pd.Series(['a','b','c'],index=[1,3,5])
# # print(data.index)
# # print(data[5])
# # print(data[1:3])

# #Solution to index confusion
# print(data.loc[3]) #implicit is loc 
# print(data.loc[1:3])

# print('================')
# print(data.iloc[2]) #implicit is iloc
# print(data.iloc[1:3])

# print("Indexing")
# index = pd.Index([1,2,3,4,6])
# print(index)
# print(index[1])
# print(index.shape)
# print(index.size)
# print(index.ndim)
# print(index.dtype)

#index are immutable 
# index[1]=3
# print(index)

# indA = pd.Index([1,2,3,4,5,6])
# indB = pd.Index([2,3,5,9,90])
# # Operation 
# print(indA & indB) #intersection 
# #union 
# print(indA | indB)
# # difference 
# print(indA ^ indB)
