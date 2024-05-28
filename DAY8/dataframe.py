import pandas as pd 

#create a dataframe with a dictionary
dict = { 
        'Name' : ['kingini','tuttu','ikka'],
        'Age':[24,23,24],
        'Place':['koovode','mavoor','punoor']
        }

#convert data into dataframes
df = pd.DataFrame(dict)

#access the name only 
print(df[['Name','Place']])

#row wise value
print(df.iloc[1])

#filtering
print(df[df['Age'] > 23])

#add a new colunm into the dataframe
df['stiphend'] = [15000,5000,5000]
print(df)

#remove a cloumn
df=df.drop(columns=['stiphend'])
print(df)

#statical functions
print(df.describe())