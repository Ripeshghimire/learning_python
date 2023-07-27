# #14.Write a program that prints all the even numbers from 1 to 50. 
# for i in range(1,51):
#     if(i % 2 == 0): 
#         print (f'The even numbers are {i}')
 
# #Create a program 
# #that calculates the sum of all the numbers from 1 to 100 using a loop.
# sum = 0
# for i in range(1,101):
#     sum = sum + i 
# print(sum)

# 1) WAP to print the sum of odd number and even numbers 1 to 20 and show which is greater

# 3) Create a program to demonstrate your phones pin checker. (break)
# oddCount = 1
# evenCount =1 
# oddSum = 0
# evenSum = 0
# while (evenCount <= 20 and oddCount <=20):
#     if(oddCount%2 == 1 ):
#         oddSum = oddSum + oddCount
#     if(evenCount%2 == 0):
#         evenSum = evenSum + evenCount
#     oddCount = oddCount + 1 
#     evenCount = evenCount + 1

# if(oddSum > evenSum):
#     print(f'The sum of odd numbers is greater {oddSum} than sum of even sum {evenSum}')
# elif(evenSum > oddSum):
#      print(f'The sum of even numbers is greater {evenSum} than sum of odd sum {oddSum}')
# else:
#     print("error")


# 2) Build a car game (break)
# Type help to request help
# Start command then print car started
# Stop command then print car stopped
# Quit command to quit the game
#
# start = "START".upper()
# quit = "QUIT".upper()
# stop = "STOP".upper()
# help = "HELP".upper()
# userInput = input("Enter what do you want to do? ").upper()

# while True:
#     userInput = input("Enter what do you want to do? ").upper()
#     if(userInput ==start ):
#         print("Car started")  
#     elif userInput == stop :
#         print("car stopped")
#     elif userInput == help:
#         print('''Please choose from the given Statement 
#               1.Start
#               2.Stop
#               3.Quit''')
#     elif userInput == quit:
#         print("Car exited")
#         break
#     else:
#         print("please try again" )



#pin checker

# pin = 9083
# count = 0 
# while (count < 3):
#     userInput = int(input("Enter the pin: "))
#     if(userInput == pin):
#         print("Unlocked")
#         break 
#     elif userInput != pin and count < 3:
#         print("Please try again ")
#     else:
#         print("You have reached maximum no of tries")
#     count = count + 1

#multiplication 
# userInput = int(input("Enter a number"))
# for n in range(1,11):
#     print(f'{userInput * n}')

#factorial of given number 
# userInput = int(input("Enter a number"))
# fact = 1 
# for i in range(1,userInput+1):
#     fact *= i
# print(fact)

# list = []
# for num in range(1,11):
#     user_input = (input("Enter the number"))
#     list.append(user_input)

# print(list)

# myList = [1,2,3,4,5,6,78,8]
# # from the given seperate the odd and even numbers in two separate list
# oddList =[]
# evenList = []
# for num in myList:
#     if num % 2 == 0:
#         evenList.append(num)
#     elif num % 2 == 1:
#         oddList.append(num)
#     else:
#         print("")
# print(f'The odd list is {oddList}')
# print(f'The even list is {evenList}')

#WAP TO separate vowel and consonent from a given string and place in list 
# user_name = input("Enter name: ")
# vowel = []
# consonant = []
# vow = {'a','e','i','o','u'}
# for name in user_name:
#     if name.lower() in vow :
#         vowel.append(name)
#     else:
#         consonant.append(name )

# print(f'The vowel list is {vowel}')
# print(f'The consonant list is {consonant}')

#from a given list of names separate the names beginning with vowels and consonent

#WAP TO separate even and odd length names form a given list 

# user_name = ["Ripesh","Roshan","Sandesh","Bagal","Bivek"]
# oddList = []
# evenList = []
# for name in user_name:
#     length = len(name)
#     if(length % 2 == 0):
#         evenList.append(name)
#     else:
#         oddList.append(name)

# print(oddList)
# print(evenList)

# name = "Ripesh"
# # print(name[::-1])

# length = len(name)
# for i in range(length-1,-1,-1):
#     print (name[i])


# Write a program to print multiplication table of a given number using for in loop
# Count the total number of digits in a number using for in loop
# Print list in reverse order using a loop do not use function
# WAP to check if the user entered string is palindrome or not

# mylist = ["Ripesh",12,"Ram","Shyam","Hari",22]
# length = len(mylist)
# reverse_list = []
# for rev in range(length-1,-1,-1):
#     reverse_list.append(mylist[rev])

# print(reverse_list)

# num =int(input("Enter a number: "))
# count = 0
# while num!=0:
#     num = num //10
#     count = count + 1 

# print(f'The number of digits in the number is {count}' )

#Palindrome 
# user_input = input("Enter the string ")
# reverse  = user_input[::-1]
# if(user_input == reverse):
#     print(f'The given string is palindrome {user_input}')
# elif(user_input !=  reverse):
#     print(f'The given string is not palindrome {user_input}')
# else:
#     print("Wrong input ")

# Given a list of strings ['apple', 'banana', 'cherry', 'date']
# , write a Python program to concatenate all the strings into one using a for loop.
# fruits = ['apple', 'banana','cherry','date']
# result = ""
# for fruit in fruits:
#     result = result + fruit
# print(f'{result}')

# num_list = [1,2,3,4,5,6]
# greater = 0
# for num in num_list:
#     greater = num
#     if greater < num :
#         greater = num 

# print(f'The greatest number is {greater}')

