#Create a function called display_info() that takes an object of either Rectangle or
# Square class and displays information about the shape (area, perimeter, diagonal if applicable).

import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

def display_info(shape):
    if isinstance(shape, Rectangle):
        print("Rectangle:")
        print("Area:", shape.calculate_area())
        print("Perimeter:", shape.calculate_perimeter())
   
    else:
        print("Invalid shape provided.")

my_rectangle = Rectangle(5, 3)
display_info(my_rectangle)