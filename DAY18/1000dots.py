import matplotlib.pyplot as plt
import numpy as np

# Generate random data for 1000 points
np.random.seed(0)  # For reproducibility
x = np.random.rand(1000)
y = np.random.rand(1000)

# Create a scatter plot
plt.scatter(x, y, color='blue', marker='o')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with 1000 Dots')

# Display the plot
plt.show()
