print("=== Welcome to Ride Builder ===")
print("1. Bike")
print("2. Car")
choice = int(input("Choose 1 or 2"))
if choice == 1:
    print("Pick your bike type")
    print("1. Mountain Bike")
    print("2. Scooty")
    bike_type = int(input("Choose 1 or 2"))
    if bike_type == 1 :
        print("Mountain Bike chosen")
        print("Have fun riding on mountains!")
    else :
        print("Scooty chosen")
        print("Have a fun scooty ride!")
elif choice==2:
    print("Pick your car type")
    print("1. Sedan")
    print("2. SUV")
    car_type = int(input("Choose 1 or 2"))
    if car_type == 1 :
        print("Sedan chosen")
        print("Get ready to have a luxurious ride")
    else :
        print("SUV chosen")
        print("Have fun off-roading!")
else :
    print("Couldn't recognize what you mean. Try again")