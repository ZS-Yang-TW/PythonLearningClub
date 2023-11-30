import math

class circle():
    def __init__(self, radius):
        self.__radius = radius
        
    @property
    def radius(self):
        return self.__radius
        
    @radius.setter
    def radius(self, radius):
        self.__radius = radius
        
    @property
    def diameter(self):
        return self.__radius * 2
    
    @property
    def area(self):
        return self.__radius**2 * math.pi
    
    @property
    def perimeter(self):
        return self.__radius * 2 * math.pi
    
    def __str__(self):
        return f"圓半徑: {self.__radius}"
    
my_circle = circle(5)
print(my_circle.radius)
print(my_circle.diameter)
print(my_circle.perimeter)
print(my_circle.area)

my_circle.radius = 10
print(my_circle.radius)
print(my_circle.diameter)
print(my_circle.perimeter)
print(my_circle.area)

print(my_circle.__radius)