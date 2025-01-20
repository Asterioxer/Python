import random

names = input("Enter Everybody's names separated by commas")
names_list = names.split(",")
print(names_list)

length = len(names_list)
randomization = random.randint(0,length-1)
print(f"{names_list[randomization]} will pay the bill")

Person_selected = random.choice(names_list) #another way
print(f"{Person_selected} will pay the bill")

print(f"{random.choice(names_list)} will pay the bill") #single line way for the previous program