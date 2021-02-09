# Example 01: Overriding object methods __str__ and operator overloading __eq__

import math 

class GeometricShape:
    def __init__(self):
        # circumference 
        self._C = 0
        # area
        self._A = 0
        self.__some_private_attribute = "Not visible outside of GeometricShape"
    
    def calculate_circumference(self):
        pass
        
    def calculate_area(self):
        pass
        
    def get_C(self):
        return self._C
        
    def get_A(self):
        return self._A

    def __str__(self):
        return f"C={self._C} A={self._A}" 
        
    def __eq__(self, obj):
        # print("Overriden __eq__")
        if type(self) == type(obj):
            return True
        return False

class Circle(GeometricShape):
    def __init__(self, radius):
        GeometricShape.__init__(self)
        self.radius = radius
     
    def calculate_circumference(self):
        self._C = 2*self.radius * math.pi
      
    def calculate_area(self):
        self._A = math.pow(self.radius, 2) * math.pi

class Rectangle(GeometricShape):
    
    def __init__(self, side_a, side_b):
        GeometricShape.__init__(self)
        self._side_a = side_a
        self._side_b = side_b
        
    def calculate_circumference(self):
        self._C = 2 * (self._side_a + self._side_b)
      
    def calculate_area(self):
        self._A = self._side_a * self._side_b 
        

class Square(Rectangle):
    
    def __init__(self, side_a):
        Rectangle.__init__(self, side_a, side_a)
        
        
if __name__ == "__main__":
    circle = Circle(2)
    
    circle.calculate_circumference()
    circle.calculate_area()
    
    print("The circumference of the shape Circle is: ", circle.get_C())
    print("Circle:", circle)
    
    rectangle = Rectangle(2, 3)
    rectangle.calculate_circumference()
    rectangle.calculate_area()
    
    print("Rectangle:", rectangle)
    
    square = Square(2)
    square.calculate_circumference()
    square.calculate_area()
    
    print("Square:", square)
     
    square2 = Square(3)
    square.calculate_circumference()
    square.calculate_area()

    print(square==rectangle)
    print(square==square2)