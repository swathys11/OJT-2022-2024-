import numpy as np 

array = np.array([10,20,30,50,40,60])

#where()
#element greater than 25 for the array
elements = np.where(array > 25, 0, array)
print(elements)
print("Elements : ",array[elements])

#element greater than 25 for the array is replaced by 0
elements = np.where(array > 25, 0, array)
print(elements)