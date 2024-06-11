import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([2, 3, 4, 5, 6, 7, 8, 9])

# Create a scatter plot
plt.scatter(x, y, color='blue', marker='o')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot Example')

# Display the plot
plt.show()
