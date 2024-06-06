import numpy as np

#original array
original_array = np.array([1,2,3,4,5,6])
print("Original Array: ", original_array)

#copy of the original array
copy_array =  original_array.copy()
original_array[2] = 9
print("Original_array after changing: ",original_array)
print("Copied array: ", copy_array)