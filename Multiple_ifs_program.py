height = int(input("Enter your height: "))
bill = 0
if height >= 3:
    print("Can Ride")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 150
        print("Pay Rs. 150 to Ride")
    elif age <= 18:
        bill = 250
        print("Pay Rs. 250 to Ride")
    else:
        bill = 500
        print("Pay Rs. 500 to Ride")

    want_photo = input("Do you want photo(Y/N)? ")
    if want_photo == 'y' or want_photo == 'Y':
        bill = bill + 50
    print(f"Your bill is {bill}")


else:
    print("You can't ride a vehicle with so less height")
print("Bye,See you soon")
print(""'Thank you,'"Enjoy your ride")