import pandas as pd

# series of data 

data=[1,5,9,7,3,1,4,6]

series = pd.Series(data)
print(series)

#access a element by indexing
print(series[3])

#arithematic operations
series_add = series + 10
print(series_add)

#filter the element in the series
filtered_series = series[series > 5]
print(filtered_series)

#statistical methods
mean = series.mean()
print("Mean value of the series is : ",mean)

median = series.median()
print("Median value of the series is : ",median)

mode = series.mode()
print("Mode value of the series is : ",mode)











# import pandas as pd

# # series of data 

# dict={"A":"Apple","B":"Banana","C":"Cherry"}

# series = pd.Series(dict)
# print(series)




























