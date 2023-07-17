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
#     if(userInput ==start):
#         print("Car started")  
#     elif userInput == stop:
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
#     count = count + 1
#     if(userInput == pin):
#         print("Unlocked")
#         break 
#     elif userInput != pin and count < 3:
#         print("Please try again ")
#     else:
#         print("You have reached maximum no of tries")

