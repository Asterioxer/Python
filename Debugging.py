#our main goal to debug any program is to understand the game of the 
#program so that it becomes convenient
#for us to understand what we wanna debug as per the 
#demands of the provided code

#import random
#dice_num = ["One","Two","Three","Four","Five","Six"]
#dice_nm = (supposedly anything the user may input)
#print(dice_num[dice_nm])

#in the code given above if the user enters dice_nm's value as 6 then the 
#indexing shifts to the seventh index which does not even exist for the list
#dice_num #it's only limited to dice_num[5] -> indexing is always taken from
#the zeroth position as a beginning

'''a,b=0,0
a=int(input("Enter a: "))
b==int(input("Enter b: ")) #the equality operator is used the reason for which the value of b which was assigned earlier is being kept constant 
product = a*b
print(f"product is {product}")'''

'''n=int(input("Enter a number: "))
if n%2 =0: #the error is present in this line where the equality was intended but was substituted by the assignment operator
   print("Even")
else:
   print("Odd")'''
