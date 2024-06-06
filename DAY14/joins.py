import numpy as np
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

join_array = np.concatenate((array1, array2))
print("Joined Array: ",join_array)

array_2D1 = np.array([[1,2,3],[4,5,6]])
array_2D2  = np.array([[7,8,9],[10,11,12]])

# join vertically - vstack()
vstack_array = np.vstack((array_2D1,array_2D2))
print("vertically joined array: ",vstack_array)

# join horizontally - hstack()
hstack_array = np.hstack((array_2D1,array_2D2))
print("Horizontally joined array: ",hstack_array)

