#Create a class Square that inherits from the Rectangle class. 
# Add a method calculate_diagonal() to calculate the diagonal of the square.

import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def calculate_diagonal(self):
        return math.sqrt(2) * self.length

# Example usage:
my_square = Square(4)
print("Diagonal of the square:", my_square.calculate_diagonal())

