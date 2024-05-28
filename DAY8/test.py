import pandas as pd    

#read the csv file into the dataframe
df = pd.read_csv('data.csv')
print(df)

#clean the row with empty data
df_cleaned_row= df.dropna(how="all")
print(df_cleaned_row)

#clean the column with empty data
df_cleaned_col=df.dropna(axis=1,how="all")
print(df_cleaned_col)

#fill the nan
df_filled_data=df.fillna(0)
print(df_filled_data)