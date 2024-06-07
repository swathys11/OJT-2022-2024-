import numpy as np

#create a 5 dimensional array
array = np.array([1,2,3,4] , ndmin=5)
print("Array of 5D: ", array)
print("Shape of the array: ", array.shape)

#verify the last element
print("Last vdimension:  ", array.shape[-1])