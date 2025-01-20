def multiply(*numbers): #args->arbitrary arguments
    c=1
    print(numbers)
    for i in numbers:
        c *= i 
    print(f"Product is {c}")

multiply(12,23)
multiply(2,3,-6,8)
multiply(2,5,8,9,0,6)