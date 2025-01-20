#A simple example
specification = ["Frank","Dustin","Soham"]
for i in specification:
    print(i)
    if i == "Soham":
        print("Soham's here")

#A complex example
numbers = [2,3,5,-10,8]
squares = []
for i in numbers:
    square = i ** 2
    squares.append(square)
    print("The list of squares is:")
    print(squares)

#set
set1 = {23,45,98,'ukraine'}
for i in set1:
    print(set1)

#list
l1 = ["Soham","Sovan","Ranjan"]
for i in l1:
    print(l1)