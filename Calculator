class Calculator():

    def __init__(self, a, b):

        self.value_1 = a
        self.value_2 = b
        

    def add(self):

       return self.value_1 + self.value_2

    def Multiply(self):

        return self.value_1 * self.value_2

    def Division(self):

        return self.value_1 / self.value_2


selection = int(input("Please select Add(1), Multiply(2) or Division(3): "))

value_1 = int(input("Value 1: "))
value_2 = int(input("Value 2: "))

result = Calculator(value_1, value_2)

if selection == 1:
    addr = result.add()
    print("For the {} and {} values you entered, the sum result is {} ".format(value_1, value_2, addr))
elif selection == 2:
    addr = result.Multiply()
    print("For the {} and {} values you entered, the multiplication result is {} ".format(value_1, value_2, addr))
else:
    addr = result.Division()
    print("For the {} and {} values you entered, the division result is {} ".format(value_1, value_2, addr))
