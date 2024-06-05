#Get the data type of an array object & Get the data type of an array containing strings

import numpy as np          

array1 = np.array([1,2,3,4,5])
datatype = array1.dtype
print("Datatype of first array: ",datatype)

array2 = np.array(["Red","Blue","Pink"])
datatype = array2.dtype
print("Datatype of second array: ",datatype)
