# myStudent = {
#     'name':'Ripesh',
#     'age':21,
#     'married' :False,
#     'grade' : None 
# }
# print(myStudent)

# myProfile  = {
#     'name' : 'Ripesh',
#     'age': 20,
#     'working':False,
#     'student' : True
# }
#Properties 
#Mutable ------- Yes
#dublication ---------- NO 
#Order --------- No 
# myProfile.pop(20)
# name = myProfile.get('name')
# print(name)
# age = myProfile.get('ages')
# print(age)

# print(myProfile)
# myProfile['age'] = 12
# myProfile['working'] = True
# myProfile['class'] = "Data Science and Machine Learning"
# myProfile.pop('student')
# print(myProfile)
# birthdays = {
#     'Ripesh': '7 Feb',
#     'Prayus': '5 Feb',
#     'Dikshya': '6 September',
#     'Ramesh': '4 July',
#     'Sushan':'8 june'
# }
# print(birthdays)
# name_ripesh = birthdays['Ripesh']
# name_dikshya = birthdays ['Dikshya']
# print(name_dikshya)
# print(name_ripesh)
# birthdays['Prayassh'] = '21 Oct'
# print(birthdays)

# for i in range(1,4):
#     name = input("Enter your name ")
#     userInput = input("Enter birthday")
#     birthdays[name] = userInput
# print(birthdays)


# for i in range (1,11):
#     if i % 2 == 0: 
#         print(i)

# num_list = ['ripesh',12,'ghimire','ama']
# for i in num_list:
#     print(i)

#Ask user a name if that name is in dictionary display 
#Bday,else add that bday and new dictionary ,end program only when user
#types quit 
# while True:
#     userInput = input("Enter a name")
#     if userInput in birthdays:#in keyword in used to check in the dictionary
#         print(birthdays)
#     elif userInput == "quit":
#         break
#     else:
#         userBday = input("Enter birthday")
#         birthdays[userInput] = userBday
#         print(birthdays)
 

# ## Ask user a name, if that name is in dictionary display Bday, else add that bday and display new dictionary, end the program only when user types quit.
# userInput = ""
# while not userInput == "quit":
    
#     userInput = input("Enter the name of user ")
#     if (userInput == "quit"):
#         break

#     dictBday = studentBirthdays.get(userInput)
 
#     if(dictBday == None):
#         userInputBday = input("Name not in dictionary enter the bday to be added ")
#         studentBirthdays[userInput] = userInputBday
#         print(f'Updated Dictionary \n {studentBirthdays}')
#     else:
#         print(f'The bday of {userInput} is {dictBday} ')
#  Write a Python script to print a dictionary that 
# contains number and square of numbers as key value pair upto 100

# Example:
# 1:1,2:4,3:9.......... 10:100
# birthdays = {
# #     'Ripesh': '7 Feb',
# #     'Prayus': '5 Feb',
# #     'Dikshya': '6 September',
# #     'Ramesh': '4 July',
# #     'Sushan':'8 june'
# # }

# numbers = {

# }
# for i in range(1,11):
#     numbers[i] = i * i 

# print(numbers)

# studentDictionary = {
#     "name" : "Ripesh Ghimire",
#     "age": 22,
#     "class" : "Python"
# }
# # #Returns the dictionary keys 
# # print(studentDictionary.keys())
# # #Returns the dictionary values 
# # print(studentDictionary.values())
# # #Return the dictionary key,as tuples insides list 
# # print((studentDictionary.items()))

# for i in studentDictionary.keys():
#     print(f'The keys in dictionary is {i}')

# marks = {
#     "maths ":10,
#     "science" :100,
#     "social" :50,
#     "english":78,
#     "nepali":70
# }
#From the above dictionary calculate the highest marks and 
#also the percentage obtained, assuming total of all subject is 100
# greater = 0
# total_marks = 0
# percentage = 0
# for marks in marks.values():
#     if marks > greater:
#         greater = marks
#     total_marks = total_marks + marks 
#     percentage = float(total_marks / 5 )
# print(f'The greatest marks is {greater}')
# print(f'The total marks is {total_marks}')
# print(f'The percentage obtained is {percentage}')

#2. Find the 
# studentDictionay = {
# "name": "Prayush Shrestha",
# "age" : 27,
# "class" : "Python Programming",
# "Programming Languages": ["Java", "Python", "JS"],
# 'Grades': [11, 12, 10, 9]
# }
# extract 10 from grades 
# grade = studentDictionay['Grades']
# # #highest grade from the dictionary
# # print (studentDictionay['Grades'][0])
# grade.sort()
# print(grade)
# highestvalue = grade[-1]
# print(highestvalue)

# teacherarray = [
#     {
#         'name' :'Ripesh Ghimire',
#         'age' : 21,
#         'subject':'Python programming'
#     }
# ]
# print(teacherarray[0]['name'])
#Create a list containing 5 students with their marks and
#  grade and subjects  as array and display all the students name with "Python" as subject.
# student_list = [
#     {
#         'name' : 'Ripesh Ghimire',
#         'username':'ripesh',
#         'age' : 22,
#         'gmail' : "ripeshghimire987@gmail.com",
#         'Programming': ["Java","Python","JavaScript"]
#     },
#     {
#         'name':'Prayush Shrestha',
#         'username':'prayush',
#         'age':27,
#         'gmail' : 'prayushrandom@gmail.com',
#         'Programming':["Java","Python","Swift"]
#     },
#     {
#         'name':'Yuddish',
#         'username':'yuddish',
#         'gmail' :'yuddishghimire@gmail.com',
#         'age' : 24,
#         'Programming' :["Rust","C#","C++"]
#     },
#     {
#         'name':'Dikshya Karki',
#         'username':'dikshya',
#         'age' : 24,
#         'gmail':'deekshyakarki567@gmail.com',
#         'Programming' :["Ruby","Python","Java"]
#     },
#     {
#         'name':'Rakshya Karki',
#         'username' : 'rakshya',
#         'age' : 24,
#         'gmail' :'rakshyakarki23@gmail.com',
#         'Programming' :["R","Julia","C"]
#     }
# ]
#Create a list containing 5 students with their marks
#  and grade and subjects  as array and display all
#  the students name with "Python" as subject.
# find = "Python"
# for i in range(0,5):
#     user_list = student_list[i]['Programming']
#     if find in user_list:  
#         print(student_list[i]['name'])

# userInput = input("Enter a language to search: ")
# username_input = input("Enter you username or gmail or age to search the data  : ") 
# for student in student_list:
#     student_name = student['name']
#     std_programming = student['Programming']
#     std_username = student['username']
#     std_gmail = student['gmail']
#     age = student['age']
#     # if userInput in std_programming :
#     #     print(f'The {student_name} is {std_programming}')
#     if username_input in std_username:
#         print(f'The gmail of the {std_username} is {std_gmail} name is {student_name} age is {age} and studies {std_programming}')
#     if username_input in std_gmail:
#           print(f'The gmail of the {std_username} is {std_gmail} name is {student_name} age is {age} and studies {std_programming}')
#     if username_input in int(age):
#           print(f'The gmail of the {std_username} is {std_gmail} name is {student_name} age is {age} and studies {std_programming}')
    
# teacherArray = [
#     {
#         "name": "Prayush Shrestha",
#         "age": 27,
#         "class": "Python Programming",
#         "Programming Languages": ["Java", "Python", "JS"],
#         'Grades': [11, 12, 10, 9]
#     },
#     {
#         "name": "Aayush Shrestha",
#         "age": 31,
#         "class": "Java Programming",
#         "Programming Languages": ["Java", "Swift", "JS"],
#         'Grades': [11, 12, 10, 9]
#     },
#     {
#         "name": "Rita Shrestha",
#         "age": 25,
#         "class": "UI UX",
#         "Programming Languages": ["HTML", "CSS", "JS"],
#         'Grades': [11, 12, 10, 9]
#     },
#     {
#         "name": "Aayusha Pokharel",
#         "age": 22,
#         "class": "Java Programming",
#         "Programming Languages": ["Python","Dart"],
#         'Grades': [11, 12, 10, 9]
#     }

# ]
  
# userKey = input("ENter the key to search in  ")
# userValue = input("Enter the value to search in ")
# for teacher in teacherArray:
#     User_Key = teacher.keys()
#     User_Values = teacher.values()
#     print(User_Values)
#     print(User_Key)
#     if userKey not in User_Key :
#         print("Please type a valid userKey to access the data ")
#     if userKey == 'age':
#         userValue = int(userValue)

#     if userKey == 'Grades':
#         if int(userValue) in teacher[userKey]:
#             print(teacher)

#     if userKey == "Programming Languages":
#         if userValue in teacher[userKey]:
#             print(teacher)

#     if teacher[userKey] == userValue:
#         print(teacher)

#create a program to uniquify the list
# num_list = [10,20,30,10,50]
# unique_list = []
# for i in num_list:
#     print(i)
#     if i not in unique_list:
#         unique_list.append(i)
# print(unique_list)
