import numpy as np

#create a 1D array
array_1D = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print("Array in 1D: ", array_1D)

#converting 1D array to 2D array
array_2D = array_1D.reshape(4,3)
print("Array of 2D: ", array_2D)