 #Write a Python program to reverse a list using a function.
def reverse_list(input_list):
    
    return input_list[::-1]
my_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(my_list)
print("Original list:", my_list)
print("Reversed list:", reversed_list)
