######MAP
#Map(function,iterable)
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
# print(len(newArray)
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
def areaOfCircle(radius,pi):
    area = pi * radius * radius
    print(f'The area of circle is {area}')
areaOfCircle(7,3.14)