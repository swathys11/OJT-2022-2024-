#starting point
#learning rate alpha
#number of iteration

#example of gradient descent
x = 10
learning_rate = 0.1
num_iteration = 100


#create a loop for gradient descent

for i in range(num_iteration):
    #compute our gradient 
    gradient = 2 * x
    
    #update the x with new parameter that is new x
    x = x - learning_rate * gradient
    print("iteration", i+1 ,": x = ",x, "f(x) = ",x**2)
print("minimum value of the x: ",x)