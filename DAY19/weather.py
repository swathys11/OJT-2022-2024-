import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("weather.csv")
data.head()

df = pd.DataFrame(data)
print(df)

# Check for and handle missing values
df.isnull().sum() 
df.dropna(inplace=True) 

# Convert the Date column to a datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Calculate statistics for the temperature using NumPy
temperature = df['Temperature'].values  
mean_temp = np.mean(temperature)
std_temp = np.std(temperature)
max_temp = np.max(temperature)
min_temp = np.min(temperature)

print("Mean: ",mean_temp)
print("Standard deviation: ",std_temp)
print("Maximum: ",max_temp)
print("Minimun: ",min_temp)

# Generate a time series plot using Matplotlib to show the temperature trend over time
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Temperature'], label='Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Temperature Trend Over Time')
plt.legend()
plt.show()


# # Create a bar chart to show the average monthly precipitation
df['Month'] = df['Date'].dt.to_period('M')
monthly_precipitation = df.groupby('Month')['Precipitation'].mean()
monthly_precipitation.plot(kind='bar', figsize=(5, 6))
plt.xlabel('Month')
plt.ylabel('Average Precipitation')
plt.title('Average Monthly Precipitation')
plt.show()


# Plot a scatter plot to examine the relationship between wind speed and temperature
plt.figure(figsize=(10, 6))
plt.scatter(df['WindSpeed'], df['Temperature'])
plt.xlabel('Wind Speed')
plt.ylabel('Temperature')
plt.title('Relationship Between Wind Speed and Temperature')
plt.show()



