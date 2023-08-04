#Functions 
#Reusable block of code 
#Declaration
#function calling 

#Syntax of declaration  ------------ def ------> keyword functionName(parameters):
# def giveMessage(): 
#     print("Hello world")
# giveMessage()

#WAP TO ASK USER HIS NAME AND PRINT IT  
# def printUser():
#     user_name = input("Enter your name: ")
#     print(f'Your name is {user_name}')
# printUser()

# def add():
#     num1 = int(input("Enter first number: ")) 
#     num2 = int(input("Enter second number: "))
#     sum = num1 + num2
#     print(f'The sum of two numbers is {sum}')
# add()

#Function with arguments and parameters 
#def functionname(argument,argument)

# def sum(num1,num2):
#     sum = num1 + num2 
#     print(f'The sum of numbers is {sum}')
# sum(2,2)

# def mul(num1,num2):
#     mul = num1 * num2
#     print(f'The multiplication of two numbers is {mul}')
# first_number = 1433434
# second_number = 23
# mul(first_number,second_number)

# def callNumber(name):
#     print(f'Called {name}')

# first_name = "Ripesh"
# callNumber(first_name)
# callNumber("Dikshya")



# Write a function for checking the speed of drivers. This function should have one parameter: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point 
# and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended”

# def checkSpeed(speed):
#     count_Point = 0
#     if speed < 70:
#         print("Ok ")
#     if speed > 70 :
#         speed = speed - 70 
#         points  = speed // 5   
#         print(f'The number of points you have gained is {points}')
#     if points > 12 :
#         print("Liscence suspended")

# checkSpeed(900)

# Write a function called showNumbers that takes a parameter called limit.
#  It should print all the numbers between 0 and limit with a label to identify the\
#  even and odd numbers. For example, if the limit is 3, it should print:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD
# def showNumbers(limit):
#     for num in range(0,limit +1):
#         if num %  2 == 0:
#             print(f'{num} EVEN')
#         if num % 2 == 1:
#             print(f'{num} ODD')

# showNumbers(3)

#WAP TO FIND THE SI (user function with argument and take input outside the function)
# principle = int(input("enter the principle amount: "))
# time = int(input("Enter the time"))
# rate = float(input("Enter the rate "))
# def simpleinterest(p,t,r):
#     si = (p*t*r)/100
#     print(f'The simple interest is {si}')

# simpleinterest(principle,time,rate)
#wap to find the area of circle (use function with argument and take input outside the function)
# user_radius = (input("Enter the radius of the circle: "))
# def findArea(radius):
#     area = 3.14  * radius * radius
#     print(f'The area of circle is {area}')
# findArea(int(user_radius))
# wap to find if a user given values id odd or even

# user_input = int(input("Enter a number"))
# def findOddorEven(num):
#     if num % 2 == 0:
#         print(f'The number is even {num}')
#     else:
#         print(f'The number is odd {num}')
# findOddorEven(user_input)
# num1 = float(input("Enter first number"))
# num2 = float(input("Enter second number"))
# userCalculation = input("Enter your operation to perform +,-,*,/")
# result = None
# def calculator(num1,num2,operator):
#     if operator == '+':
#         result = num1 + num2
#     elif(operator == '-'):
#         result = num1 - num2
#     elif operator == '*':
#         result = (num1 * num2 )
#     elif operator == '/':
#         result = (num1/num2)
#     else:
#         print("Please chosse from the above operators")
#     if result != None:
#         print(f'The calculation of {num1} {operator} {num2} is {result} ')
# calculator(num1,num2,userCalculation)

# Write a Python function to find the maximum of three numbers.
# def findgreaterst(a,b,c):
#     if a > b and a > c :
#         print(f'The greatest no is {a}')
#     elif b > c and b > a :
#         print(f'The greatest no is {b}')
#     elif c > a and c >b :
#         print(f'The greatest no is {c}')
#     else:
#         print ("error")
# first_num = int(input("Enter the first number: "))
# second_num = int(input("Enter the second number: "))
# third_num = int (input("Enter the third number: "))
# findgreaterst(first_num,second_num,third_num)

# write a program to check if a given value is in a array or no 
# user_list = [1,3,22,23,23,23]
# def find(num): 
#     if num in user_list:
#         print(f'The number is found {num}')
#     else:
#         print(f'The number is not found ')

# userInput = int(input("Enter a number: "))
# find(userInput)

# array = [2,4,6,8,10]
# def multiply(n):
#     for num in array:
#         print(f'{num} * {n} = {(num * n)} ')

# multiply(2)
# print("==================")
# multiply(5)

# put in new array
# array = [2,4,6,8,10]
# array1 = []
# def multiply(n):
#     for num in array:
#         mul = n * num
#         array1.append(mul)
#     print(array1)
# multiply(2)

# def changeToNegative(value):
#     return value * -1
# def addNumber(value):
#     return value + 5 

# result = addNumber(12)
# result2 = changeToNegative(result)
# print(result2)
# print("=============Next Execution=====")
# result = addNumber(55)
# print(result)

#wap to calculate each member of array of value   by a givenNumber
#and change to above 
# array = [2,4,6,8,10]
# array1 = []
# def multiply(n):
#     for num in array:
#         mul = n * num
#         array1.append(mul)


# #wap to calculate is si the final result of one exection in npr and inr 
# def si(p,t,r):
#     interest = (p*t*r)/100
#     return interest

# npr = si(10,10,30)
# print(f'The nepalese rupees of interest is {npr}')
# inr = npr * 1.6
# print(f'The indian rupees is {inr}')
# inr = si(20,40,234)
# print(f'The indian interest of the given value is {inr}')


#WAP to get only even number from and array using 
# function and display it in new array
# user_lit = [23,12,24,523,352,124,56,57,2,2325234234,1212313,3124]
# even_list = []
# def onlyEven():
#     for num in user_lit:
#         if num % 2 == 0:
#             even_list.append(num)
            
#     return even_list

# even = onlyEven()
# print(even)
#------------------------------------------------------------------
# def multiply(num1,num2):
#     return num1 * num2
# mul = multiply(2,3)
# print(f'The multiplication of two numbers is {mul}')
#-------------------------------------------------------------------
# def mySqrFunction(num):
#     return num * num 
# sqrt = mySqrFunction(2)
# print(f'The square of the given no is {sqrt}')
#----------------------------------------------------------------------
# def simpleFunction(firstname,middlename,lastname):
#     result = f'{firstname} {middlename} {lastname}'
#     print(result)
# simpleFunction("Ripesh", middlename="Ghimire",lastname="Karki")
# simpleFunction(firstname="sushan",lastname="Shrestha",middlename="stha")
# simpleFunction(lastname="Ghimire",firstname="Ripesh",middlename="uzu")
# simpleFunction(lastname="Karki",firstname="Dikshya",middlename="zzuuuzuzu")
#------------------------------------------------------------------------
                        # Multiple Parameters at a time using args 
# def myFnctn(*args):
#     for x in args:
#         print (x)

# myFnctn(2,2,32,23,23,2,3,23,23,23,23)
# myFnctn(1,21,2,1,21,2)
#--------------------------------------------------------------------------
# def array(*args):
#     new_list= []
#     for x in args:
#         new_list.append(x)
#     print(new_list)
# array(2,23,23,23,23,23,23,43,41,21,212,313,4332,424,343)
# array(24,3245,24,223)
#---------------------------------------------------------------------------
#kwargs
# def myFunction(**kwargs):
#     print(kwargs)
#     print(kwargs['num1'])
# myFunction(num1=1,num2=12,num3=23)
#-------------------------------------------------------------------------------
#wap to aceepts firstnam, and age  and adrress as kwargs argument and display int he given format 
# hi the name is prayush.I am 27 and from ktm
# def showName(**teacher):
    # print(teacher)
    # first_name = teacher['firstname']
    # age1 = teacher['age']
    # address1 = teacher['address']
    # print(f"Hi the name is {teacher['firstname']}.I am {teacher['age']} from {teacher['address']}")
    # print(f'hi the name is {first_name}. I am {age1} from {address1}')

# showName(firstname = "Prayush",age = 27 ,address = "ktm")
#-----------------------------Default argument--------------------------------------------------
# def areaOfCircle(radius,pi=3.14):
#     area = pi * radius * radius
#     print(f'The area of circle is {area}')
# areaOfCircle(7
#----------------------------------------------------------------------
# Write a function to double a given number ( Use return and argument )
# def square(num1):
#     sqrt = num1 * num1 
#     return sqrt
# print(square(2))
# Write a function to return cube of a given number.
# def cube(num1):
#     return num1 * num1 * num1
# cub = cube(9)
# print(cub)
# Write a function to return true if a number is even and false if odd
# def findevenorOdd(num):
#     if num % 2 == 0:
#         return True
#     elif num % 2 == 1:
#         return False
#     else:
#         print("Eroor no")
# eoro = findevenorOdd(2)
# # print(eoro)
# Create the following  array myArray = [1,2,3,4,5,8,10,12,9,11]
# user map in first and second quesion to double and triple and store in new array
# User filter in third question
# myArray = [1,2,3,4,5,8,10,12,9,11]
# result = map(square,myArray)
# print(list(result))
# cubic = map(cube,myArray)
# print(list(cubic))
# Even = filter(findevenorOdd,myArray)
# print(f'The filtered numbers are ')
# for e in Even:
#     print (e)
# odd = filter(lambda x:x%2==1,myArray)
# for i in odd:
#     print(i)
