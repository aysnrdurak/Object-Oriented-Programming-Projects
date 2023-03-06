from abc import ABC, abstractmethod

class shapes:
    @abstractmethod 
    def Area(self, ): pass

    @abstractmethod
    def perimeter(): pass

    def toString(): pass

#child class
class Square(shapes):
    def __init__(self, edge):
        self.__edge = edge

    def area(self):
        result = self.__edge**2
        print("Square Area: ", result)

    def perimeter(self): 
        result = self.__edge*4
        print("Square Peirmeter: ", result)

    #override ve polymorphism 
    def toString(self):
        print("Square edge: ", self.__edge)

        
class circle(shapes):
    "Circle class"
    PI = 3.14 
    # Constant variable -> hiçbir yerde değişmeyecek değişkenlerdir. 
    # Eğer büyük harfle tanımlanmışsa bu bir constant variable dır.

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        result = self.PI*self.__radius**2
        print("Circle area: ", result)

    def perimeter(self):
        result = 2*self.PI*self.__radius
        print("Circle perimeter: ", result)

    def toString(self):
        print("Circle Radius: ", self.__radius)


c = circle(5)
c.area()
c.perimeter()
c.toString()

s = Square(5)
s.area()
s.perimeter()
s.toString()
