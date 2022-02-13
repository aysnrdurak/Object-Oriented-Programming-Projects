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
islem = input("Yapmak istediğiniz islem toplama ise (1)'i, çarpma ise (2)'yi, ikisi ise (3)'ü tuşlayınız.")

c1 = Calculator(v1, v2)
result1 = c1.add()
result2 = c1.multiply()

if islem == "1":
    print("Toplam: ", result1)

elif islem == "2":
    print("Çarpım: ", result2)

elif islem == "3":
    print("Toplam: {}, Çarpım: {}".format(result1, result2))
