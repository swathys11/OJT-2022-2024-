import matplotlib.pyplot as plt

#data
x = [1, 2, 3, 4, 5]
y = [2, 3, 6, 7, 10]

#create a plot with marker
plt.plot(x,y, marker = 'D', linestyle = '-.', color = 'blue', markersize = 6, markerfacecolor = 'r')

#add labels, tites
plt.title('Line plot with markers')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()