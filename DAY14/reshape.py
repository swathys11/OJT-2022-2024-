#convert 1D array to 2D array
#.reshape() is used to reshaping the array
import numpy as np         

#create 1D array
array_1D = np.array([1,2,3,4,5,6])
print("Array1D: ", array_1D)
print("Shape of the array1D: ", array_1D.shape)

#reshape th 1D array to 2D array
array_2D = array_1D.reshape(2,3)
print("2D array: ", array_2D)
print("shape of the array2D: ",array_2D.shape)

#reshape the 1D array to 3D
array_3D = array_1D.reshape(3,2)
print("3D array: ", array_3D)
print("shape of the array3D: ",array_3D.shape)


#reshape 2D to 1D
array_1D = array_2D.reshape(-1)
print("Array1D: ", array_1D)
print("shape of the array1D: ",array_1D.shape)