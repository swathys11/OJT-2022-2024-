import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
    
    def calculate_diagonal(self):
        return math.sqrt(2) * self.width  
square = Square(5)
print(f"Area: {square.area()}")  
print(f"Perimeter: {square.perimeter()}") 
print(f"Diagonal: {square.calculate_diagonal()}")  
