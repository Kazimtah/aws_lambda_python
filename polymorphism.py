# Polymorphism
import math 
class Shape:
    def calc_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius 

    def calc_area(self):
        return math.pi *self.radius **2 
    
class Rechtangle(Shape):
    def __init__(self, widht, height):
        self.width = widht
        self.height = height 
    
    def calc_area(self):
        return self.height* self.width
        
shapes = [Circle(5), Rechtangle(10,2), Circle(10), Rechtangle(44,5)]

for shape in shapes:
    print(shape.calc_area())
#first_circle = Circle(5)
#print(first_circle.calc_area())