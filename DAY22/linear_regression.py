import numpy as np
from sklearn.linear_model import LinearRegression

#Data points
x= np.array([1,2,3,4,5]).reshape(-1,1)
y= np.array([2,3,5,7,11])

#create linear regression model
model = LinearRegression()
model.fit(x, y)

# Predict the value of y when x = 6
x_new = np.array([[6]])
y_pred = model.predict(x_new)

print(f"Predicted value of y for x = 6: {y_pred[0]}")







