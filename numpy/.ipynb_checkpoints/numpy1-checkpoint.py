import numpy as np 
#creating a numpy array 
#syntax
#variable = np.array([])
# normal_list = [1,2,3,4,5]
# print (normal_list)
# print(type(normal_list))
# print("############################")
# array = np.array([1,2,3,4,4,5],dtype = int)
# print(type(array))
# print(array)

#heirarchy in 
#none 
#boolean 
#int 
#float
#string
# zeros  = np.zeros(10,dtype=int)
# print(zeros)
# ones = np.ones(20,dtype=int)
# print(ones)
#create a custom array 
# customArray = np.full(10,2,dtype=str)
# print(customArray)
#create a custom array for size 21 with value *
# customArray = np.full(20,'*',dtype=str)
# print(customArray)
#create a csut

#multi dimensional aray 
# array = [
#     [1,2,3,4,5],
#     [3,32,32,43]
#   ]
# myMulti = np.array(array)
# print(myMulti)
# rng = np.random.default_rng(seed= 0)
# print(rng)
# random_array = rng.integers(low = 8,high =200,size = (3,5),dtype = int,endpoint = True)
# random_array = rng.integers(1,10,size=(3,5))
# print(random_array)
# random_array = rng.integers(100,200,size=(10,10))
# print(random_array)
# print(random_array[-1][3])

#-------------------------------------Numpy array attributes---------------------------
# x1 = np.array([1.2,2.1,3.1,34.0,5.0])
# x2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(x1)
# print(x2)
# #shape -----------no of rows and colums 
# print(f'the shape of x1 is {x1.shape}')
# print(f'The shape of x2 is {x2.shape}')
# #size
# print(f'The size of x1 is {x1.size}')
# print(f'the size of x2 is {x2.size}')
# #ndim
# print(f'The dimensions of x1 is {x1.ndim}')
# print(f'THe dimension of x2 is {x2.ndim}')
# #nbytes
# print(f'TTHe nbytes of x1 is {x1.nbytes}')
# print(f'TTHe nbytes of x2 is {x2.nbytes}')
# #dtype 
# # print(f'THe dtype of x1 is {x1.dtype}')
# # print(f'THe dtype of x2 is {x2.dtype}')
#

# multidimensionalArray = np.array([[12,1,2,3],[4,5,6,7],[8,9,10,11]])
# [[12 1 2]
#  [4 5 6 ]]

# print(multidimensionalArray[:2,:3])
#
# [[12  2]
#  [ 4  6]
#  [ 8 10]]
# print("----------------")
# print(multidimensionalArray[:,::2])

# [[4]]
# print("----------------")
# print(multidimensionalArray[1:2,0:1])


# multidimensionalArray = np.array([
#     [12,1,2,3],
#     [4,5,6,7],
#     [8,9,10,11]])

# [[11 10  9  8]
#  [ 7  6  5  4]
#  [ 3  2  1 12]]

# print("----------------")
# print(multidimensionalArray[::-1,::-1])
#concatination of array
# x = np.array([1,2,3])
# y = np.array([4,5,6])
# z= np.array([7,8,9])
#concationation of arary 
# concanitated_array = np.concatenate([x,y,z])
# print(concanitated_array)
#multidimensional array concatination
# grid = np.array([[1,2,3],[4,5,6]])
# grid2 = np.array([[8,9,10],[11,12,13]])
# concanited_grid = np.concatenate([grid,grid])
# print(concanited_grid)

#  VSTACK
# while doing vstack no of colums should be same
# concationation2 = np.concatenate([grid,grid2],axis = 0)
# print(concationation2)
# vconcanitate = np.vstack([grid,grid2])
# print(vconcanitate)
print('==========================================')
#HSTACK 
# while doing hstack no of rows should be same
# concationation2 = np.concatenate([grid,grid2],axis=1)
# hconcanitate = np.hstack([grid,grid2])
# print(hconcanitate)
# print(concationation2)
# print('=================================')
# x = np.array([1,2,3])
# grid = np.array([[11,22,33],[4,5,6]])
# v = np.hstack([grid,x])
# print(v)

#Splitting in numpy 
# c = np.array([1,2,3,4,5,6,7,8,9])
# x,y = np.split(c,[2])
# print(x)
# print(y)
#Another example 
# x1,x2,x3,x4 =np.split(c,[2,4,5])
# print(x1)
# print(x2)
# print(x3)
# print(x4)
#------------------------------------------
# grind = np.arange(16).reshape(4,4)
# upper,mid,lower = np.vsplit(grind,[1,3])
# print(upper)
# print("==========")
# print(mid)
# print("==========")
# print(lower)

# left,centre,high = np.hsplit(grind,[1,3])
# print(left)
# print("==========")
# print(centre)
# print("==========")
# print(high)
#practise question
# with open (r'files/filehandling/Marks.rtf','r') as file:
#     numbers = file.readlines()
#     num_list = []
#     print(numbers)
#     num_list = list(map(lambda x : int(x),numbers))
#     print(num_list)
    # for num in numbers:
    #     num_list.append(int(num))
# x = np.array(num_list)
# print(np.min(x))
# print(np.max(x))
# print(np.std(x))
# print(np.mean(x))
# print(np.percentile(x,90))
# print(np.percentile(x,10))
# print(np.median(x))
# print(np.percentile(x,25)) #first quartile 
# print(np.add.reduce(x))
# print(np.add.accumulate(x))
z = np.array([1,2,3,4,5,6,np.nan])
#none 
print(z)
print(np.nansum(z))