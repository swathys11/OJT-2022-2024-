import numpy as np

# Create a 2D NumPy array
arr2d = np.array([[0, 1, 2, 3, 4],
                  [5, 6, 7, 8, 9],
                  [10, 11, 12, 13, 14],
                  [15, 16, 17, 18, 19]])

# Access a specific element (row 1, column 2)
element = arr2d[1, 2]

# Slice a sub-array (rows 1 to 3, columns 2 to 4)
sub_array = arr2d[1:3, 2:5]
print(sub_array)