# Object oriented programming 
# class and object 
# class is a  blueprint and object is instance of class 
# every object has attributes properties------k cha ? k garcha?
# class Mammals:
#     heartChamber = 4
#     givesBirth = True
#     scientific_name = "Mammalia"

# Instancing object
# cow = Mammals()
# print(cow.heartChamber)
# WAP to create a class name car with different properties such as
#  wheeltype,no of seats,color etc and create 2 objects of the same
# class car:
#     no_of_seats = 4
#     color = "blue"
#     wheeltype = "alloy"
# nissan = car()
# range_rover = car()
# print(nissan.color)
# print(range_rover.color)
#----------------------------------Constructor calling in python-------------------------
# class Car :
#     wheel = 4
#     seatbelt = True
#     color = ''
#     company = ''
#     def __init__(self,co,com) :
#         self.color = co 
#         self.company = com
# jeep = car("green","maruti")
# print(jeep.color)
#create a class student include school and dress as common parameters
#name age and class from constructor
# class Student:
#     name = ''
#     age = 0
#     classes = 0
#     school = "Reliance Co -Ed "
#     dress = "Red"
#     def __init__(self,na,ag,cls):
#         self.name = na
#         self.age = ag
#         self.classes=cls
#     def __str__(self):
#         return(f"{self.name} is of {self.age}")
#     #--------------------------Methods------------------------
#     def greet(self):
#         print(f"Hello my name is {self.name}.My age is {self.age}")

# Ram = Student("ripesh",23,7)
# print(Ram)
# print(Ram.classes)
# print(Ram.age)
# print(Ram.dress)
# Ram.greet()
#----------------------------------Calculator-------------------------
# class Calculator:
#     num1 = 0
#     num2 = 0
#     def __init__(self,num1,num2) :
#         self.num1 = num1 
#         self.num2 = num2
#     def add(self):
#         return self.num1 + self.num2
#     def subtract(self):
#         return self.num1 - self.num2
#     def divison(self):
#         return self.num1 / self.num2 
#     def product(self):
#         return self.num1 * self.num2
# Operation = Calculator(5,5)
# print(Operation.add())
#----------------------------------Inheritance---------------------------------------------
# class Father:
#     caste = "shresthat"
#     def __init__(self,name):
#         self.name = name
#     def fatherfunction(self):
#         print("Hello I am father")
# class Children(Father):

#     def __init__(self,gender,name):
#         self.gender = gender
#         super().__init__(name) 
#     def childFunction(self):
#         print("Hello I am child")
# c1 = Children()
# c1.fatherfunction()
# c1.childFunction()
#--------------------------------------Rectangle--------------------------------------
# class Rectangle:
#     length = 0 
#     breadth = 0
#     def __init__(self,length,breadth):
#         self.length = length
#         self.breadth = breadth
#     def area(self):
#         area = self.length * self.breadth
#         print(f"The area of rectangle is  {area}")
#     def perimeter(self):
#         perimeter = 2 * (self.length+self.breadth)
#         print(f'The perimeter of rectangle is {perimeter}')
# r1 = Rectangle(10,10)
# r1.area()
# r1.perimeter()
# ) WAP which includes attributes like name, country and
# date of birth.Write a method to determine the person's age
# from datetime import datetime
# class Person:
#     def __init__(self,name,country,dob):
#         self.name = name 
#         self.country = country
#         self.dob =dob
#     def age(self):
#         current_date = datetime.now()
#         age = current_date - self.dob



# WAP to create a class that represents a shape.Write methods calculate its area and perimeter. Also 
# have subclasses for different shapes like circle, triangle, and square.
# class Shape:
#     def circle(self,radius):
#         area = 3.14 * radius * radius
#         print(f"The area of circle is  {area}")
#     def Rectangle(self,length,breadth):
#         area = length * breadth 
#         print(f'The area of rectange is {area}')
#     def Square(self,length):
#         area = length * length
#         print(f'The area of square is {area}')
#     def triangle(self,breadth,height):
#         area = 0.5 * breadth * height
#         print(f'The area of triangle is {area}')
# class Rectangle(Shape):
#     def findarea():
#         print("")
# r1 = Rectangle()
# r1.Square(23)