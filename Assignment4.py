from abc import ABC, abstractmethod

class diamentions():
     def __init__(self, base = 0, height = 0,length = 0,breadth = 0):
        self.height = height
        self.base = base
        self.length = length
        self.breadth = breadth
        pass
        
class Polygon(ABC, diamentions):
    @abstractmethod
    def area(self):
        pass

class Triangle(Polygon):
    def area(self):
        area = (self.base * self.height) / 2
        print("Area Of Triangle : {0}".format((area)))
        pass

class Rectangle(Polygon):
    def area(self):
        area = self.length * self.breadth
        print("Area Of Rectangle : {0}".format(area))
        pass


base = int(input("Enter base of Triangle: "))
height = int(input("Enter height of Triangle: "))
triangle = Triangle(base,height)
triangle.area()

print("---------------------------------------")

len = int(input("Enter length of Rectangle: "))
width = int(input("Enter breadth of Rectangle: "))
rectangle = Rectangle(length= len, breadth= width)
rectangle.area()

print("---------------------------------------")

dim = diamentions(base, height,len,width)