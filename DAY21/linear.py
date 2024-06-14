import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#dataset
height = np.array([150,160,164,165,173]).reshape(-1,1)
weight = np.array([50,65,63,68,72])

#create an linear regression model for the above dataset
model = LinearRegression()

#lets fit the model with approprite data

model.fit(height,weight)

predicted_weight = model.predict(height)

print("Intercept: ", model.intercept_)
print("coefficients: ", model.coef_[0])

#create a scatterplot for the above
plt.scatter(height,weight, color='blue')
plt.plot(height,predicted_weight, color ='red')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Linear Regresssion')
plt.show()
