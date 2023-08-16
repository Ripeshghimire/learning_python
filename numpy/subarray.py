import numpy as np
# x1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# xsub = x1[:2,:2]
# xsub[0][0] = 90
# print(x1)
####copying array 
# print("sub copy")
# xsub_copy = x1[:2,:2].copy()
# xsub_copy[0,0] = 22
# print(xsub_copy)
# print(f'the main array is\n {x1}')


#-----------------------------------------_Reshaping a array 
# array = np.arange(1,10)
# print(array)
#reshape 
# x2 = array.reshape(3,3)
# print(x2)
#
#adding a dimension in an array 
# x3 = np.array([1,2,3])

# x5  = x3[np.newaxis,:]
# print('----------')
# print(x5)
# print('-------------------')
# x6 = x3[:,np.newaxis]
# print(x6)