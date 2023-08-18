# Numpy Refresher Questions
import numpy as np 
# 1.	Create a null vector or size 10.
null_array = np.zeros(10)
print(null_array)
# 2.	Create a null vector of size 10 but the fifth value which is 1
null_array = np.zeros(10)
null_array[4]  = 1 
print(null_array)
# 3.	Create a vector with values ranging from 10 to 49
range_array = np.arange(10,50)
print(range_array)
# 4.	Reverse a vector (first element becomes last)
reverse_array = range_array[::-1]
print(reverse_array)
# 5.	Create a 3x3 matrix with values ranging from 0 to 8
matrx = np.arange(9).reshape(3,3)
print(matrx)
# 6.	Find indices of non zero elements from [1,2,0,0,4,0]
x = np.array([1,2,0,0,4,0])
nonzero = np.nonzero(x)
print(nonzero)
# 7.	Create a 3x3 identity matrix
print(np.identity(3))
# 8.	Create a 3x3x3 array with random values
print(np.random.randint(10,20,(3,3,3)))
# 9.	Create a 10x10 array with random values and find the minimum and maximum
random_array = np.random.randint(10,20,(10,10))
print(np.max(random_array))
print(np.min(random_array))

# 10.	Create a random vector of size 30 and find the mean value
random_array = np.random.randint(low=0,high=30,size=(1,30))
print(np.mean(random_array))
# 11.	Given a 1D array, negate all elements which are between 3 and 8, in place.
x = np.array([1,2,4,4,5,6,7,8,9,10])

# 12.	Create a random vector of size 10 and sort it
rng = np.random.default_rng(seed=101)
array = rng.integers(0,10,(1,10))
print(array)
print(np.sort(array))

# 13.	Make an array immutable (read only)

