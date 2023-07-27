#1. Write a Python program to find those numbers which are divisible by 7
# and multiples of 5, between 1500 and 2700 (both included).

# numbers = []
# for num in range(1500,2701):
#     if num % 7 == 0 and num % 5 == 0:
#         numbers.append(num)

# print(numbers)

#2 . Write a Python program to guess a number from 1 to 9 
#import random
# a = int(input("Guess the number:"))
# random_element = random.randint(1,11)
# #print(random_element)
# if a <= 10 and a > 0 :
#     if a == random_element:
#         print(f'You have guessed the number correctly! {random_element}')  
#     else:
#        print(f'you guessed wrong {random_element}')
# else:
#     print("Please choose between 1 to 10  ")


#3.Write a Python program that accepts a word from the user and reverses it.
# user_word = input("Enter the word ")
# reversed_word = user_word[::-1]
# print(reversed_word)
 
# 4.Write a Python program that iterates the integers from 1 to 50.
# For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz".
# For numbers that are multiples of three and five, print "FizzBuzz".
# num = int(input("Enter a number"))
# if num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print(num)

#5.write a python program to check the username and password a check 
# input_user = input("Enter the username ")
# input_password = input("Enter the password ")
# username= "RIPESH"
# password = "Oakland@123"
# if(input_user.upper() == username and input_password == password):
#     print("Welcome to the Profile")
# elif(input_user.upper()== username and input_password!=password):
#     print("Password wrong")
# elif(input_user.upper()!= username and input_password == password ):
#     print("Username wrong")
# else:
#     print("username and password wrong.Please Try again")

# 6.write a python program to reverse a given input no 
# input_number = int(input("Enter a number"))
# reverse_number = 0
# while(input_number!= 0):
#     rem = input_number % 10 
#     reverse_number  = (reverse_number * 10 )+ rem
#     input_number = input_number // 10 
#     print(input_number)



#7. Write a python program to check whether the given no is positive negative or zero
# input_number = int(input("Enter a number"))
# if(input_number>1):
#     print(f'The number is positive {input_number}')
# elif(input_number<0):
#     print(f'The number is negative {input_number}')
# else:
#     print(f'The number is zero {input_number}')

#8. Write a Python program to find the greatest and smallest number between the given set of three numbers 
# first_num = int(input("Enter a number"))
# second_num = int(input("Enter the second number"))
# third_num = int(input("Enter the third number "))
# if first_num > second_num and first_num > third_num:
#     print(f'{first_num} is the greatest')
# elif second_num >first_num and  second_num > third_num :
#     print(f'{second_num} is the greatest ')
# elif third_num > first_num and third_num > second_num:
#     print(f'{third_num} is the greatest ')
# elif third_num == second_num == first_num:
#     print("All are equal")
# elif third_num 

# checking the smallest number
# if first_num <second_num and first_num < third_num:
#     print(f'{first_num} is the smallest')
# elif second_num < third_num :
#     print(f'{second_num} is the smallest')
# else:
#     print(f'{third_num} is the smallest ')

# 9 .WAP to create a program that takes the desired field from the user 
#and gives knowledge about the course 
# user_hm = input("Enter your interested field")
# if(user_hm == "SERVICE"):
#     print("You can take the service course")
# elif(user_hm == "HOUSEKEEPING"):
#     print("You can take the housekeeping service")
# elif user_hm.upper() == "KITCHEN":
#     print("You can take the chefs course")
# else:
#     print("Please choose from the gives course that i provided you ")
 
# 10.wap to check the a
# user = input("Are you a teacher or student")
# age = int(input("What is your age"))
# if user.upper() == "TEACHER" or user.upper()=="STUDENT":
#     print("You can vote")
# else:
#     print("You cannot vote")
 
# 0 - 80 
#80-100 
#11. WAP to create lucky draw with multiple prizes giving weight
# import random
# user_money = int(input("Do you want to play the lottery. Please pay Rs.10: "))
# random_number = random.randint(0,100)

# if(user_money == 10):
#     if(random_number == 5 ):
#         print(f'You have won the lottery. The winning number is  {random_number}')
#     elif(random_number > 0 and random_number<=40):
#         print(f'You have won a car {random_number}')
#     elif(random_number>40 and random_number <= 60):
#         print(f'Better Luck Next Time')
#     else:
#         print(f'You have won a apple product. The winning number is  {random_number} ')
# else:
#     print("Please pay the money to play the lucky draw")

#12.Create a function that counts the number of elements within a list that are greater than 30.
# num = [1,4,62,78,32,23,90,24,2,34]
# length = len(num)
# # print(num[::-1])
# # print(type(num))
# # #for n in num:
# # if 1 in num:
# #     print("Yes")
# for i in range(length):
#     if (num[i]>35):
#         print (num[i])
    
# 13.Assign 8 to the variable x and 15 to the variable y.
# In the same cell, create 2 conditional statements.

# Let the first one print "At least one of the conditions is satisfied." if x is greater than 3 or y is even.

# Let the second one print "Neither condition is satisfied." if x is less than or equal to 3 and y is odd.

# Change the values assigned to x and y and re-run the cell to verify your code still works.
# x = 1
# y = 15
# if x > 3 or y % 2 == 0:
#     print("At least one condition is satisfied")
# elif x <3 or y % 2 ==1 :
#     print("Neither condittion is satisfied")

# wap to check if a given number is multiple of 3 or not 
#wap to check if a given number is multiple of 5 or not
# num = int(input("Enter a number"))
# if num==0:
#     print("You cannot enter zero ")
# elif (num % 3 == 0) and (num % 5 == 0):
#      print("FizzBuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:f
#     print(f'It is not the multiple of both numbers {num}')

#. wap to ask use with a  amount and display how many bills of each 


