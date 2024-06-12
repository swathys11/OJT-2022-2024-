import matplotlib.pyplot as plt

#Data
x = [1,2,3,4,5]
y1 = [1,4,9,16,25]
y2 = [1,2,3,4,5]

#create the plot
plt.plot(x,y1, linestyle = '-', color = 'blue', linewidth = 3, marker = 'o', markersize = 8, markerfacecolor= 'orange')
plt.plot(x,y2, linestyle = '--', color = 'red', linewidth = 3, marker = 'X', markersize = 8, markerfacecolor= 'yellow')

plt.title("Customized line plot with grid")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

#create a legend method with the chart
plt.legend()
#Add the value as grid
plt.grid(True)

#customize the grid
plt.grid(color='grey', linestyle='--', linewidth=1)
plt.show()