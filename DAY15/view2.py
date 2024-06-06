import numpy as np

#original array 
original_array = np.array([1,2,3,5,8,9,5,4])
view_array = original_array.view()
print("View array: ", view_array)
view_array[3] = 12
print("View array after changing: ", view_array)