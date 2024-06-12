import matplotlib.pyplot as plt                     

#dataset
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

#create a plot for the dataset
plt.plot(x,y)

#customization for the plot

#add a title 
plt.title("Line Plot")

#add labels
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

#output
plt.show()
