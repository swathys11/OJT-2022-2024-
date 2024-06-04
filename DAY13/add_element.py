# Get third and fourth elements from an array and add them
import numpy as np          
array = np.array([1, 2, 3, 4, 5])
third_fourth = array[2:4]
sum = np.sum(third_fourth)
print(sum)