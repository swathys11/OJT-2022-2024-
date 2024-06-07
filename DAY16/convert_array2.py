import numpy as np

#create 1D array
array_1D = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print("Array of 1D: ", array_1D)

#convert 1D array to 3D array
array_3D = array_1D.reshape(2,3,2)
print("Array of 3D: ", array_3D)