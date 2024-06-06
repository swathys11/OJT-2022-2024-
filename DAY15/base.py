import numpy as np
#original array 
original_array = np.array([1,4,7,8,9,5,2,3,6])
print("Original array: ", original_array)

#copy of the array
copy_array = original_array.copy()
print("Copies array: ", copy_array)

#view of the array
view_array = original_array.view()
print("View array: ", view_array)