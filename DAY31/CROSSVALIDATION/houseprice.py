import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

#load our data
df = pd.read_csv('housing_price.csv')

#split the dataset into feature and target as (x) and (y) axis

x = df[['size', 'bedrooms']].values
y = df['price'].values

#initiate or define our model
model = LinearRegression()

#define our crossvalidation method which is KFold
kf = KFold(n_splits=5)

mean_scores = []

for train_index, test_index in kf.split(x):
    x_train, x_test = x[train_index], x[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
    #training the model with set which we gets after looping
    model.fit(x_train, y_train)
    
    #predict the test set
    y_pred = model.predict(x_test)
    mean = mean_absolute_error(y_test, y_pred)
    mean_scores.append(mean)
average_mean = np.mean(mean_scores)
print("Average Mean Absolute Error: ", average_mean)
