#child class ların ortak olarak barındırdığı tüm özellikler
#parent classımız içerir.

class Animal:
    def __init__(self):
        print("Animal created")

    def toString(self):
        print("Animal")

    def walk(self):
        print("Animal can walk")

#child class

class Bird(Animal): #Parantez içine hangi parent'e ait olduğunu yazarız
    def __init__(self):
        super().__init__() #use init of parent(animal) class
        print("Bird created")
      
    def toString(self):
        print("Bird")

    def fly(self):
        print("Bird can fly")


b1 = Bird()
b1.toString()
b1.walk()
b1.fly()

class Monkey(Animal):
    def __init__(self):
        super().__init__()
        print("Monkey created")

    def climb(self):
        print("Monkey can climb")

m1 = Monkey()
m1.climb()

class Sparrow(Bird):
    def __init__(self):
        super().__init__()
        print("Sparrow created")

    def Tiny(self):
        print("Sparrow is tiny")

s1 = Sparrow()
s1.Tiny()
