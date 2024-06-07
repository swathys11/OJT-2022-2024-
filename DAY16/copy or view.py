import numpy as np

#create a 1D array
array_1D = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

#convert the 1D array to 2D array
array_2D = array_1D.reshape(4,3)
is_view = np.may_share_memory(array_1D,array_2D)
print("The array_2D is view of array_1D: ", is_view)

array_2D[0,2] = 24
print("Array_1D: ", array_1D)
print("Array_2D: ", array_2D)