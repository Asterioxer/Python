import math
def paint_calculation(width,height,cover):
    area = height*width
    no_of_cans = math.ceil(area/cover)
    print(f"You will need {no_of_cans}")
h = int(input("Enter the height of the wall: "))
w = int(input("Enter the width of the wall: "))
coverage = 7

paint_calculation(width= w,height= h, cover= coverage)

