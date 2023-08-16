import numpy as np 
# x = np.array([1,2,3,4])
# y = np.array([2,22,32,1])
# print(f'Great')
# print(x>y )
# print(f'Less')
# print(x<y)
# print(f'Eqaual')
# print(x==y)
# print(f'not equal to')
# print(x!=y )

#-----------------------------
# result = (2*x) == (x**2)
# print(result)
#----------------------------------------
# myMulti_array = np.arange(0,16).reshape(4,4)
# print(myMulti_array)
# print(myMulti_array>16)

#random array and finding 
rng = np.random.default_rng(seed=101)
x = rng.integers(0,10,(3,4))
# print(x)
# print("number of values that are greater that 4")
# print(np.sum(x>4))
#
# print("number of values that are greater than 4 in rows")
# print(np.sum(x>4,axis=1))
# print("number of values that are greater than 4 in rows")
# print(np.sum(x>4,axis=0))
#check if any value is greater that 100

print("check if any value is grater that 100")
print(np.any(x>100))
print("check if all value if less than 100 or not")
print(np.all(x<100))