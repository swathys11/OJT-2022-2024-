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

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
    
    def calculate_diagonal(self):
        return math.sqrt(2) * self.length

def display_info(shape):
    if isinstance(shape, Rectangle):
        print("Rectangle:")
        print("Area:", shape.calculate_area())
        print("Perimeter:", shape.calculate_perimeter())
    elif isinstance(shape, Square):
        print("Square:")
        print("Area:", shape.calculate_area())
        print("Perimeter:", shape.calculate_perimeter())
        print("Diagonal:", shape.calculate_diagonal())
    else:
        print("Invalid shape provided.")


# my_rectangle = Rectangle(5, 3)
# display_info(my_rectangle)

my_square = Square(4)
display_info(my_square)
