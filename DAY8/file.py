import pandas as pd    

#read the csv file into the dataframe
df = pd.read_csv('data.csv')
print(df)

df = pd.read_csv('data.csv',
                 #for give the datatypes
                 dtype={'Age':int,'Salary':float},
                 #read specific columns
                 usecols=['Name','Age','Place'])
print(df)