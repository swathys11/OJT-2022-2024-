# Convert the file into a dataframe
 
# create filter based on the country
# find the median mean std for the respective column and store into a new column
# delete the the repeated entries
# change the null values into 0

import pandas as pd

df = pd.read_csv('air-pollution.csv')

# Specify the country and column names
country_column_name = 'Entity' 
country_filter = 'India' 
pollution_column_name = 'Nitrogen oxide (NOx)'  

# Filter based on the specified country
filtered_df = df[df[country_column_name] == country_filter].copy()

# Calculate median, mean, and standard deviation for the specified column
median_value = filtered_df[pollution_column_name].median()
print("Median",median_value)

mean_value = filtered_df[pollution_column_name].mean()
print("Mean",mean_value)

std_value = filtered_df[pollution_column_name].std()
print("std",std_value)

# Add the calculated values as new columns
filtered_df.loc[:, 'Median'] = median_value
filtered_df.loc[:, 'Mean'] = mean_value
filtered_df.loc[:, 'Std'] = std_value

# Remove duplicate entries
filtered_df = filtered_df.drop_duplicates()
print(filtered_df)

# Replace null values with 0
filtered_df = filtered_df.fillna(0)
print(filtered_df)


df_csv= filtered_df.to_csv('filtered_air_pollution.csv', index=False)

print(df_csv)