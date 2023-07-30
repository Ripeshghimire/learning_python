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
def findgreaterst(a,b,c):
    if a > b and a > c :
        print(f'The greatest no is {a}')
    elif b > c and b > a :
        print(f'The greatest no is {b}')
    elif c > a and c >b :
        print(f'The greatest no is {c}')
    else:
        print ("error")
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
third_num = int (input("Enter the third number: "))
findgreaterst(first_num,second_num,third_num)
