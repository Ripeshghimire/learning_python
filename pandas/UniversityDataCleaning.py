import numpy as np 
import pandas as pd
from openpyxl.workbook import Workbook 
universityTown = []
with open (r'numpy/numpy and pandasfile/university_towns.txt','r') as file:
    fileData = file.readlines()
for line in fileData:
    if'[edit]' in line:
        state = line
    else:
        universityTown.append((state,line))
townsdf = pd.DataFrame(universityTown,columns=['State','Region'])
# print(townsdf)
def getCity(item):
    if '(' in item:
        return item[:item.find(' (')]
    elif '[' in item:
        return item[:item.find('[')]
    else:
        return item

townsdf2 = townsdf.applymap(getCity)
print("=================")
# print(townsdf2)
def getUniversity(item):
    if '(' in item:
        return item[item.find('(')+1:item.find(')')]
    
townsdf3 = townsdf.applymap(getUniversity)
print(townsdf3)
townsdf2['University'] = townsdf3['Region']
print(townsdf2)
townsdf2.to_excel('student.xlsx')