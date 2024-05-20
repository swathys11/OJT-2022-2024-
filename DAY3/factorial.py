#Write a Python program to calculate the factorial of a number using a lambda function and reduce function
from functools import reduce
multiply = lambda x, y: x * y
def factorial(n):
    if n == 0:
        return 1
    return reduce(multiply, range(1, n + 1))
number = 5
result = factorial(number)
print("The factorial of ",number ," is ",result)
