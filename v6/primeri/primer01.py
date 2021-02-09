# Example 01: Inheritance (Single Inheritance) and Polymorphism

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


class Circle(GeometricShape):
    def __init__(self, radius):
        GeometricShape.__init__(self)
        self.radius = radius
     
    def calculate_circumference(self):
        self._C = 2*self.radius * math.pi
      
    def calculate_area(self):
        self._A = math.pow(self.radius, 2) * math.pi

# Example 02: Inheritance (Multilevel Inheritance) and Polymorphism

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


# Example 03: Polymorphism
def c_a_of_geo_shape(geo_shape):
    shape = ""
    if isinstance(geo_shape, Circle):
        shape = "Circle"
    elif isinstance(geo_shape, Square):
        shape = "Square"
    elif isinstance(geo_shape, Rectangle):
        shape = "Rectangle"
    else:
        shape = "Geo-shape"
        
    print(f"{shape}: the circumference is {geo_shape.get_C()} and area is {geo_shape.get_A()}")
        
        
if __name__ == "__main__":
    circle = Circle(2)
    
    circle.calculate_circumference()
    circle.calculate_area()
    
    print("The circumference of the shape Circle is: ", circle.get_C())
    c_a_of_geo_shape(circle)
    
    rectangle = Rectangle(2, 3)
    rectangle.calculate_circumference()
    rectangle.calculate_area()
    
    c_a_of_geo_shape(rectangle)
    
    square = Square(2)
    square.calculate_circumference()
    square.calculate_area()
    
    c_a_of_geo_shape(square)
    
    # if we uncomment the line below we get the following error: AttributeError: 'Circle' object has no attribute '__some_private_attribute'
    #print(circle.__some_private_attribute)