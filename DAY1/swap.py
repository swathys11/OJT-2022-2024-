num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

print("Before swapping")
print("num1:",num1)
print("num2:",num2)
print("After swapping")

num1=num1 + num2
num2=num1 - num2
num1=num1 - num2

print(num1)
print(num2)
