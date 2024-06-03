import numpy as np 

#created an array
array_2D = np.array([[1,2,3],
                     [4,5,6]])

#accessing a single element
element = array_2D[1,2]
print("element at the index of [1,2]: ",element)

#access by 2 row
row = array_2D[1:]
print("Second row: ",row)

#access by 1 row
row = array_2D[0,:]
print("First row: ",row)

#access the 2 colomn
col=array_2D[:,1]
print("Second colomn: ",col)

#slicing
#access the subarray with row of 0 and 1, column of 1 and 2
slice_array = array_2D[0:2,1:3]
print("Subarray: ",slice_array)