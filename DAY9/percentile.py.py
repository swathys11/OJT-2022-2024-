import numpy as np

# Sample data
data = np.array([15, 20, 35, 40, 50])

# Calculate specific percentiles
percentiles = [25, 50, 75]
percentile_values = np.percentile(data, percentiles)

print("Percentiles and their values:")
for p, value in zip(percentiles, percentile_values):
    print(f"{p}th percentile: {value}")
