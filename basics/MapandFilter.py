# #--------------------------------------------MAP---------------------------------------------
# # variable = (function-reference, myArray) 
# #Map(function,iterable)
# myArray = [12,23,34,56,12,3]
# newArray = []
# def multiplyBy2(value):
#     return value * 2
# for item in myArray:
#     res = multiplyBy2(item)
#     newArray.append(res)
# print(newArray)
# newArray =  list(map(multiplyBy2,myArray))
# print(len(newArray))
# newArray =  filter(multiplyBy2,myArray)
# print(len(newArray))
# # Write a function to double a given number ( Use return and argument )
# def square(num1):
#     sqrt = num1 * num1 
#     return sqrt
# print(square(2))
# # Write a function to return cube of a given number.
# def cube(num1):
#     return num1 * num1 * num1
# cub = cube(9)
# print(cub)
# # Write a function to return true if a number is even and false if odd
# def findevenorOdd(num):
#     if num % 2 == 0:
#         return True
#     elif num % 2 == 1:
#         return False
#     else:
#         print("Eroor no")
# eoro = findevenorOdd(2)
# print(eoro)
# Create the following  array myArray = [1,2,3,4,5,8,10,12,9,11]
# user map in first and second quesion to double and triple and store in new array
# User filter in third question
myArray = [1,2,3,4,5,8,10,12,9,11]
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

# myArray = [1,2,3,4,5,8,10,12,9,11]
# result = map(lambda num1:num1*num1,myArray)
# print(list(result))
# cube = map(lambda num1 :num1* num1 * num1,myArray)
# print(list(cube))
# odd = list(filter(lambda x:x%2==1,myArray))
# even = list(filter(lambda num:num%2 == 0,myArray))
# print(even)