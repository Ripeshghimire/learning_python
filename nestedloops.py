
# # #Nested Loop 
# for i in range(1,13):
#     print("===================")
#     for j in range(1,11):
#         print(f'{i} * {j} ={(i*j)}')

# value1  = [1,2,4,5,6]
# value2 = [2,4,6,8,10]
# #wap to find the combinations of value1 and value 2 
# for i in value1:
#     for j in value2:
#         print(f'({i},{j})' )

# myArray=[
#     ["Ram","Shyam","Hari","Gopal"],
#     ["Radhe","Sita","Geeta","Rita"]
# ]
# for name in myArray:
#     # print(name)
#     for name1 in name:
#         print(f'The name is  {name1}')

# separate name with odd and even len in the word two different list 
# oddList = []
# evenList = []
# for outer in myArray:
#     for inner in outer:
#         if len(inner) % 2 == 0:
#             evenList.append(inner)
#         else:
#            oddList.append(inner)      
# print(evenList)
# print(oddList) 
# teacherArray = [
#     {
#         "name": "Prayush Shrestha",
#         "username":"prayush",
#         "age": 27,
#         "class": "Python Programming",
#         "Programming Languages": ["Java", "Python", "JS"],
#         'Marks': [100, 89, 90, 91]
#     },
#     {
#         "name": "Aayush Shrestha",
#         "age": 31,
#         "username": "ayush",
#         "class": "Java Programming",
#         "Programming Languages": ["Java", "Swift", "JS"],
#         'Marks': [88, 79, 90, 91]
#     },
#     {
#         "name": "Rita Shrestha",
#         "age": 25,
#         "married":"False",
#         "username": "rita",
#         "class": "UI UX",
#         "Programming Languages": ["HTML", "CSS", "JS"],
#         'Marks': [70, 89, 90, 91]
#     },
#     {
#         "name": "Aayusha Pokharel",
#         "age": 22,
#         "username": "aayusha",
#         "class": "Java Programming",
#         "Programming Languages": ["Python", "Dart"],
#         'Marks': [80, 89, 92, 91]
#     }

# ]


# for teacher in teacherArray:
#     greater = 0 
#     teacher_marks = teacher['Marks']
#     username = teacher['name']
#     total_marks = 0
    
#     fullmarks = len(teacher_marks) * 100
#     for marks in teacher_marks:
#         total_marks  = total_marks + marks 
#     per = float((total_marks / fullmarks) * 100)
#     if per > greater :
#         greater = per
# print(f'THe greatest is {greater}')
#     # print(f'The percentage of  {username} is {per}')
