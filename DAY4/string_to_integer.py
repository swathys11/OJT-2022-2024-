# Write a Python program with a function that converts a string to an integer.
# Handle exceptions within the function and print appropriate error messages
def string_to_integer(s):
    try:
        return int(s)
    except ValueError:
        print("Error: Input string is not a valid integer.")
input_string = input("Enter a string to convert to integer: ")
integer_value = string_to_integer(input_string)
if integer_value is not None:
    print("Integer value:", integer_value)
