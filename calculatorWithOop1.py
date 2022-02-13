class Calculator(object):
    def __init__(self, a, b):
        self.value1 = a
        self.value2 = b

    def add(self):
        return self.value1 + self.value2

    def multiply(self):
        return self.value1 * self.value2

v1 = int(input("ilk değer: "))
v2 = int(input("ikinci değer: "))

c1 = Calculator(v1, v2)
result1 = c1.add()
result2 = c1.multiply()

print("Toplam {} ve çarpım {} değerleridir.".format(result1, result2))