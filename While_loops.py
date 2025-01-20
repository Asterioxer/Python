total = 0
num = int(input("enter a number(-1 to quit)"))
while num != 0:
    total += num
    num = int(input("enter a number(-1 to quit)"))
print(f"Total is {total}")