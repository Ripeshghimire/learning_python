import pandas as pd
from openpyxl.workbook import Workbook
dobMonth = {
   '101':'1',
   '102':'12',
   '103':'11',
   '104':'09',
}
dobYear = {
   '101':'1996',
   '102':'1998',
   '103':'1996',
   '104':'1997'
}

dobday = {
   '101':'1',
   '102':'2',
   '103':'10',
   '104':'23',
}
marks = {
   '101': 50,
   '102': 90,
   '103': 30,
   '104': 40,
}
graceMarks = {
   '101': 5,
   '102': 0,
   '103': 15,
   '104': 10,
}
monthSeries = pd.Series(dobMonth,name='month')
# print(monthSeries)
yearSeries = pd.Series(dobYear)
daySeries = pd.Series(dobday)
marksSeries = pd.Series(marks)
graceSeries = pd.Series(graceMarks)
# print(marksSeries) 
# print(monthSeries) 
total_marks = marksSeries + graceSeries
result = total_marks / 4 
print(result)
for values in result.values:
   if values > 40 :
    result = 'Pass'
   else:
    result = 'Fail'

# total_marks = list(map(lambda x : marksSeries.values+ graceSeries.values,marks.keys()))
# print(total_marks)

df = pd.DataFrame({'month':monthSeries,'year':yearSeries,'day':daySeries,'marks':marksSeries,'grace':graceSeries,'total':total_marks,'result':result})
print(df)
df.to_excel('student.xlsx')