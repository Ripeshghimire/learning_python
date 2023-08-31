import numpy as np 
import pandas as pd 
book_df = pd.read_csv('numpy/numpy and pandasfile/BL-Flickr-Images-Book.csv')
# print(book_df)
# print(book_df.columns)
# works 
# 1.Remove unnecessary columns 
columns_to_drop = ['Edition Statement','Contributors','Corporate Author','Corporate Contributors','Former owner','Engraver','Shelfmarks' ]
book_df.drop(columns=columns_to_drop,inplace=True)
# print("After dropping")
# print(book_df.columns)
# 2.find column that is unique
remaining_colums = book_df.columns
nullandUnique = []
for col in remaining_colums :
    if book_df[col].is_unique and np.sum(book_df[col].isnull() == 0):
        nullandUnique.append(col)
print(nullandUnique)
# 3.Change the index to isbn or identifier
book_df.set_index('Identifier', inplace= True)
# print(book_df.index)
# print(book_df.iloc[12])
# 4.columns to appropriate data types 
# print(book_df.dtypes)
#----------------------------------------using regex 
regex =  r'(\d{4})'
dop  = book_df['Date of Publication']
satisifieddata = dop.str.extract(regex,expand= False)
print(satisifieddata)
book_df['Date of Publication'] = pd.to_numeric(satisifieddata)
print(book_df.dtypes)


# Place of publications 
placeOfPublication = book_df['Place of Publication']
print(placeOfPublication.loc[157633])

london = placeOfPublication.str.contains('London')
oxford = placeOfPublication.str.contains('Oxford')
# print(london)
# print(oxford)

print("Issues Data")
print(book_df.loc[4157862])
print(book_df.loc[4159587])
#np.where(cond,True,Flas)
book_df['Place of Publication'] = np.where(london,'London',
                                                   np.where(oxford,'Oxford',
                                                            placeOfPublication.str.replace('-',' ')))
print(book_df['Place of Publication'].sample(10))


print(book_df.loc[4157862])
print(book_df.loc[4159587])