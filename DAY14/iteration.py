import numpy as np 

#for-in loo
array_1D = np.array([1,2,3,4,5,6])
#iterate the elememnts in the array
print("Array_1D: ",array_1D)

for elements in array_1D:
    print(elements)
               

#2D array
array_2D = np.array([[1,2,3],[4,5,6]])
print("Array_2D: ",array_2D)

# for row in array_2D:
#     for elements in row:
#         print(elements)
        
for elements in np.nditer(array_2D):
    print(elements)
    
#iterate elements with the index 
for index, element in np.ndenumerate(array_2D):
    print("index: ", index ," Element: ",element)