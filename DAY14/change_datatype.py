#Change data type from float to integer by using 'i' as parameter value

import numpy as np 
# Create a float array
float_array = np.array([1.1, 2.2, 3.3, 4.4], dtype=np.float64)

# Change data type from float to integer using 'i' as parameter value
int_array_i = float_array.astype('i')
print("Array with data type changed from float to integer using 'i':", int_array_i)
print("Data type:", int_array_i.dtype)
