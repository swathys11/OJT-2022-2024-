#Change data type from float to integer by using int as parameter value

import numpy as np
# Change data type from float to integer using int as parameter value
float_array = np.array([1.1, 2.2, 3.3, 4.4], dtype=np.float64)
int_array_int = float_array.astype(int)
print("Array with data type changed from float to integer using int:", int_array_int)
print("Data type:", int_array_int.dtype)
