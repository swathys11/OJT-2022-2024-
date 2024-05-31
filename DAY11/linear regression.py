import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = np.array([[1], [2], [3], [4], [5]]) 
y = np.array([2, 3, 5, 7, 11])  

model = LinearRegression()
model.fit(x, y)

y_pred = model.predict(x)
plt.scatter(x, y, color='blue', label='Actual data')
plt.plot(x, y_pred, color='red', label='Fitted line')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Simple Linear Regression')
plt.legend()
plt.show()










import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression

x=[[1],[2],[3],[4],[5]]
y=[7,8,9,6,4]

model=LinearRegression()
model.fit(x,y)

y_pred=model.predict(x)
plt.scatter(x,y,color='blue', label='Scatterplt')
plt.plot(x,y_pred, color='red',label='fitted line')
plt.show()