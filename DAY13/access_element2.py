#Access the third element of the second array of the first array
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
third_element = arr[0, 1, 2]
print(third_element)