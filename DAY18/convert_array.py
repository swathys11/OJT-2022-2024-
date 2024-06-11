import numpy as np 
#create 1D array
array_1D = np.array([1,2,3,4,5,6,7,8])

array_3D = array_1D.reshape(2,2,2)
print("3D array: ", array_3D)