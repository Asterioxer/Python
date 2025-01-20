size = input("What size of Pizza do you want(S/M/L)? ")
bill = 0
if size == 'S' or size == 's':
    bill += 100
    print("Small Size pizza costs Rs.100 ")
elif size == 'M' or size  == 'm':
    bill += 200
    print("Medium Size pizza costs Rs.200 ")
else:
    bill += 300
    print("Large Size pizza comes for Rs.300")
want_pepperoni = input("Do you want Pepperoni(Y/N)? ")
if want_pepperoni == 'Y' or want_pepperoni == 'y':
    if size == 's' or size == 'S':
        bill += 30
    else:
        bill += 50
want_extracheese = input("Do you want extra cheese(Y/N)? ")
if want_extracheese == 'Y' or want_extracheese == 'y':
    bill += 20
print(f"Your Total bill amoount is {bill}")