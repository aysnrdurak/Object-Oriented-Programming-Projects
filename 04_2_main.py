from 04_1_rent import CarRent, BikeRent, Customer
bike = BikeRent(100)
car = CarRent(10)
customer = Customer()

main_menu = True

while True:

    if main_menu:
        print(""" 
        ***** Vehicle Rental Shop *****
        B. Bike Menu
        C. Car Menu
        Q: Exit
        """)
        # main mmanu içindeyken herhangi bir şeye basarsam manim manu kapansın demek için aşağıdaki komutu yazıyoruz.
        main_menu = False
        choice = input("Enter Choice: ")

    if choice == "B" or choice == "b":
        print("""
        ***** Bike Menu *****
        1. Display available bikes
        2. Request a bike on hourly basis € 5
        3. Request a bike on daily basis € 84
        4. Return a bike
        5. Main Menu
        6. Exit
        """)
        choice = input("Enter choice: ")

        try: 
            choice = int(choice)
        except ValueError:
            print("It is not integer")
            continue

        if choice == 1:
            bike.displayStock()
            choice == "B"

        elif choice == 2:
            customer.rentalTime_b = bike.rentHourly(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 1
            main_menu = True
            print("------------------------------------------")
            
        elif choice == 3: 
            customer.rentalTime_b = bike.rentDaily(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 2
            main_menu = True
            print("------------------------------------------")

        elif choice == 4:
            customer.bill = bike.returnVehicle(customer.returnVehicle("bike"), "bike")
            customer.rentalBasis_b, customer.rentalTime_b, customer.bikes = 0,0,0
            main_menu = True

        elif choice == 5:
            main_menu = True

        elif choice == 6:
            break

        else:
            print("Please just write number until 6")
            main_menu = True


    elif choice == "C" or choice == "c":
        print("""
        ***** Car Menu *****
        1. Display available cars
        2. Request a car on hourly basis € 10
        3. Request a car on daily basis € 192
        4. Return a car
        5. Main Menu
        6. Exit
        """)
        choice = input("Enter choice: ")

        try: 
            choice = int(choice)
        except ValueError:
            print("It is not integer")
            continue

        if choice == 1:
            bike.displayStock()
            choice == "C"

        elif choice == 2:
            customer.rentalTime_c = car.rentHourly(customer.requestVehicle("car"))
            customer.rentalBasis_c = 1
            main_menu = True
            print("------------------------------------------")
            
        elif choice == 3: 
            customer.rentalTime_c = car.rentDaily(customer.requestVehicle("car"))
            customer.rentalBasis_c = 2
            main_menu = True
            print("------------------------------------------")

        elif choice == 4:
            customer.bill = car.returnVehicle(customer.returnVehicle("car"), "car")
            customer.rentalBasis_c, customer.rentalTime_c, customer.cars = 0,0,0
            main_menu = True

        elif choice == 5:
            main_menu = True

        elif choice == 6:
            break

        else:
            print("Please just write number until 6")
            main_menu = True

    elif choice == "Q" or choice == "q":
        break

    else:
        print("Invalid input please select B, C or Q")
        main_menu = True

    print("Thank youuu")

