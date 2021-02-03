import math


# Assignment 1
# Create a class that represents a circle
# calculate the O = ? and P = ? of a  circle
class Circle:
    def __init__(self, radius):
        self.r = radius
        self.C = 0
        self.A = 0

    def calculate_circumference(self):
        self.C = 2 * self.r * math.pi

    def calculate_area(self):
        self.A = math.pow(self.r, 2) * math.pi

    def print_result(self):
        self.calculate_circumference()
        self.calculate_area()
        print(f"C = {self.C}, A = {self.A}")


# Assignment 2
class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.sideB = side_b
        self.A = 0
        self.C = 0

    def calculate_circumference(self):
        self.C = 2 * self.side_a + 2 * self.side_b

    def calculate_area(self):
        self.A = self.side_a * self.side_b

    def print_result(self):
        self.calculate_circumference()
        self.calculate_area()
        print(f"C = {self.C}, A = {self.A}")


# Assignment 3
class Square:
    def __init__(self, side_a):
        self.sideA = side_a
        self.A = 0
        self.C = 0

    def calculate_circumference(self):
        self.C = 4 * self.side_a

    def calculate_area(self):
        self.A = math.pow(self.side_a, 2)

    def print_result(self):
        self.calculate_circumference()
        self.calculate_area()
        print(f"C = {self.C}, A = {self.A}")


if __name__ == '__main__':
    circle = Circle(4)
    circle.print_result()

    rectangle = Rectangle(2, 3)
    rectangle.print_result()

    square = Square(2)
    square.print_result()
