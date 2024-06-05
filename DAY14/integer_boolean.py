#Change data type from integer to boolean

import numpy as np
# Create an integer array
int_array = np.array([0, 1, 2, 3, 4])

# Change data type from integer to boolean
bool_array = int_array.astype(bool)
print("Array with data type changed from integer to boolean:", bool_array)
print("Data type:", bool_array.dtype)
