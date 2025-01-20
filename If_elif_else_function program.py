height = int(input("Enter your height: "))

if height >= 3:
    age = int(input("Enter your age: "))
    if age < 12:
        print("Can't Ride, Underage")
    elif age <= 18:
        print("Pay Rs. 250 to Ride")
    else:
        print("Pay Rs. 500 to Ride")

else:
    print("You can't ride a vehicle with so less height")
    print("Bye,See you soon")
    