import numpy as np  
import matplotlib.pyplot as plt                       
from sklearn.linear_model import LogisticRegression 

x=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
y=np.array([0,0,0,0,0,1,1,1,1,1])

model=LogisticRegression()
model.fit(x,y)

y_pred=model.predict(x)
y_prob=model.predict_proba(x)[:,1]

print("Predicted class label: ", y_pred)
print("Predicted probability: ", y_prob)

plt.scatter(x,y, color="blue")
plt.plot(x,y_prob, color="red")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()