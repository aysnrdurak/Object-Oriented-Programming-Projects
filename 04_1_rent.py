import datetime

#Parent class
class VehicleRent:

    def __init__(self, stock):
        
        "Stoch should be integer value and it means how many vehicle we have"

        self.stock = stock
        self.now = 0

    def displayStock(self):

        print("{} vehicle available to rent". format(self.stock))
        return self.stock
        
        
    def rentHourly(self, n):
        """n means is vehicle count"""

        if n <= 0:
            print("Number should be positive")
            return None

        elif n > self.stock:
            print("Sorry {} vehicle available to rent".format(self.stock))
            return None

        else:
            self.now = datetime.datetime.now()
            print("Rented {} vehicle for hourly at {} hours".format(n, self.now.hour))

            self.stock -= n
            return self.now

    def rentDaily(self, n):

        "n means is vehicle count"

        if n <= 0:
            print("Number should be positive")
            return None

        elif n > self.stock:
            print("Sorry {} vehicle available to rent".format(self.stock))
            return None

        else:
            self.now = datetime.datetime.now()
            print("Rented a {} vehicle for daily at {} hours".format(n, self.now.hour))

            self.stock -= n
            return self.now

    def returnVehicle(self, request, brand):
        
        car_h_price = 10
        car_d_price = car_h_price*8/10*24
        bike_h_price = 5
        bike_d_price = bike_h_price*7/10*24

        rentalTime, rentalBasis, numberOfVehicle = request
        bill = 0

        if brand == "car":
            if rentalTime and rentalBasis and numberOfVehicle:
                self.stock += numberOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime 

                if rentalBasis == 1:
                    bill = rentalPeriod.seconds/3600*car_h_price*numberOfVehicle

                elif rentalBasis == 2:
                    bill = rentalPeriod.seconds/(3600*24)*car_d_price*numberOfVehicle

                if (2 <= numberOfVehicle):
                    bill = bill*0.8

                print("Price: € {} ".format(bill))
                return bill

        elif brand == "bike":
            if rentalTime and rentalBasis and numberOfVehicle:
                self.stock += numberOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime 

                if rentalBasis == 1:
                    bill = rentalPeriod.seconds/3600*bike_h_price*numberOfVehicle

                elif rentalBasis == 2:
                    bill = rentalPeriod.seconds/(3600*24)*bike_d_price*numberOfVehicle

                if (4 <= numberOfVehicle):
                    bill = bill*0.8

                print("Price: € {} ".format(bill))    
                return bill      

        else:
            print("Error! Please contact with somebody from this company.")   
            return None                  

#Child Class
class CarRent(VehicleRent):

    #global variable tanımlamak
    global discount_rate
    discount_rate = 15

    def __init__(self, stock):
        super().__init__(stock)

    def discount(self):      
        bill = b - (b*discount_rate)/100
        return bill

#Child class
class BikeRent(VehicleRent):

    def __init__(self, stock):
        super().__init__(stock)        


class Customer:

    def __init__(self):
        
        self.bikes = 0
        self.rentalBasis_b = 0
        self.rentalTime_b = 0

        self.cars = 0
        self.rentalBasis_c = 0
        self.rentalTime_c = 0

    def requestVehicle(self, brand):
        "take a rquest bike or car from customer"
        if brand == "bike":
            bikes = input("How many bikes would you ike to rent? ")

            # hata alma olasılığın varsa try ve except kullnılır
            try:
                bikes = int(bikes)
            
            except ValueError:
                print("Number should be Number")
                return -1

            if bikes < 1:
                print("Number of bikes should be greater than zero")
                return -1

            else:
                self.bikes = bikes

            return self.bikes
        
        elif brand == "car":
            cars = input("How many cars would you ike to rent? ")

            # hata alma olasılığın varsa try ve except kullnılır
            try:
                cars = int(cars)
            
            except ValueError:
                print("Number should be Number")
                return -1

            if cars < 1:
                print("Number of cars should be greater than zero")
                return -1

            else:
                self.cars = cars

            return self.cars
        else: 
            print("Error!")

        

    def returnVehicle(self, brand):

        if brand == "bike":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b, self.rentalBasis_b, self.bikes
            else:
                return 0,0,0

        elif brand == "car":
            if self.rental_time_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c, self.rentalBasis_c, self.cars
            else:
                return 0,0,0
        else:
            print("Return vehicle Error")
        
