#File modes
#Read mode 
#Write mode 
#Append mode 

#-----------------------------------------Reading a file---------------------------------
#Steps 
#Get the path of the file 
#open the file in specified mode 
# filePath = r'files/hello.txt'
# myFile  = open(filePath,'r')
# Perform Operation 
# fileContent = myFile.read()
# print(type(fileContent))
# # print(fileContent)
# fileContent1 = myFile.readlines()
# print(fileContent1)
# fileContent2 = myFile.readline()
# print(fileContent2)
#-----------------------------------------Writing to a file---------------------------------
# filePath = r'files/ripesh.txt'
# fileWrite = open(filePath , 'w')
# fileWrite.write("This is ripesh Ghimire how are you brother")
#-----------------------------------------Appending to a file---------------------------------
# file = open(filePath,'a')
# fileappend = file.write("\n hi how are you ") 
#--------------------------wap to ask user username afnd pass and store it in a file---------------------------------
# filewrite = open('filePath','w')
# username = input("Enter your name: ")
# password = input("Enter you password")
# filewrite.writelines(username )
# filewrite.writelines(password)
#------------------------------------------------------------------------------------------
#----------------- WAP to write name of 5 people in file asking input from the user-------
# with open('files/name.txt' ,'w') as file :

#     for i in range (1,6):
#      userInput = input("Enter you name: ")
#      file.write(userInput)
#      file.write("\n")


## Assuming that the file contents all the marks of grade 11 students, 
# calculate the percentage,grade,highest,lowest marks
# with open(r'files/FilleMarks.txt', 'r') as file:
#     marks1 = file.readlines()
#     marks = [int(mark) for mark in marks1]  # Convert strings to integers
#     marks.sort()
#     print(marks)
#     highest = marks[-1]
#     lowest = marks[0]
#     print(f'The highest marks is {highest}')
#     print(f'The lowest marks is {lowest}')
#     total_marks = 0
#     for mark in marks:
#         total_marks += mark
#     percentage = total_marks/len(marks)
#     print(percentage)
#     if (percentage > 80):
#         grade = "A"
#     elif(percentage>60):
#         grade = "B"
#     elif percentage >= 40:
#         grade = "C"
#     elif percentage > 0:
#         grade = 'f'
# with open(r'files/information.txt','w') as file:
#     file.write("The highest marks is ")
#     file.write(str(highest))
#     file.write("\n")
#     file.write("The lowest marks is ")
#     file.write(str(lowest))
#     file.write("\n")
#     file.write("the percentage is")
#     file.write(str(percentage))
#     file.write("\n")
#     file.write("The grade is")
#     file.write(grade)
#     file.write('\n')
    

#and store in a file
# WAP to create a simple billing system
# 1) Display the menu to user from file
# 2) Create a dictionary with same menu items key as item and price as value
# 3) In loop until user enters quit ask user item and quantity to order and store 
# 4) display a bill with 13% vat and store in file
# def showMenu():
#     with open(r'files/menu.txt','r') as file:
#         menu = file.read()
#         print(f'The menu is \n {menu}')
#showMenu() 
# menu = {
#     'momo':120,
#     'chowmein':140,
#     'fried rice': 150,
#     'sizzler':450
# }
# def takeOrder():
#       with open(r'files/userorder.txt' , 'w')as file:
#        while True: 
#         showMenu()
#         userInput = input("what would you like to have: ")
#         keyList = list(menu.keys())
#         if userInput == 'quit':
#             break
#         with open(r'files/userorder.txt' , 'a') as file:
#             for order in keyList:
#                 if userInput in order:
#                     file.write(userInput+'\n')
            

# takeOrder()
# def display():
#    with open(r'files/userorder.txt','r') as file:
#     keyList = list(menu.keys())
#     user_order = file.readlines() #gets the things that have been ordered 
#     print(user_order)
#     amount= 0
#     for order in user_order:
#         order = order.strip()
#         if order in keyList:
#             # print(order,menu[order])
#             amount += menu[order]
#     total_amount = amount + (amount/100)*13
#     print(f'Your total bill is {total_amount}')
# display()    
#    total_amount = 
# def diction():
#     menu = {}
#     with open(r'files/menu.txt','r') as file:
#         for menu in file:
#             key,value = menu.strip().split(':')
#             menu[key] = value
#         print(menu)
# diction()

# 5)Write a program to create a searching algorithm
# ( Assume that the text is store in a file )

# def Search():
#     userInput = input("What would you like to search in the the file: ")
#     with open (r'files/Searchfile.txt','r') as file:
#         fileread = file.readline()
#         print(fileread)
#         if userInput in fileread:
#             print(f'found the word in {userInput}')
# Search()