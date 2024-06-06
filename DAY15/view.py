import numpy as np 

#original array
original_array = np.array([1,2,3,3,4,5,8])
print("Original array: ", original_array)

#view array
view_array = original_array.view()
original_array[5] = 10
print("Original array after change: ", original_array)
print("View array: ",view_array)