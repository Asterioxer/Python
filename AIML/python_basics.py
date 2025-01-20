import math
#variable
var = int(input("Enter a number: "))
#condition
if var % 2 == 0:
    print("Even")
else:
    print("Odd")   
#loop
for var in range(1,11):
    print(var)
#function
def primenum(var):
    is_prime = True
    if var == 1:
        is_prime = False
    for i in range(2,math.ceil(var/2)+1):
        if var%i==0:
            is_prime = False
    if is_prime == True:
        print("It is a Prime Number")
    else:
        print("It is not a prime number")

primenum(11)

#list
l = [1,10,-8,0,43,-56]
print(-7 not in l)
print(-8 in l)
print(10 not in l)

#set
set1 = {23,45,98,'ukraine'}
for i in set1:
    print(set1)

#tuple
t1 = (1,10,-8,0,43,-56)
print(-7 not in t1)
print(-8 in t1)

#dictionary
d1 = {'a':1,'b':10,'c':-8,'d':0,'e':43,'f':-56}
print('a' in d1)
print('b' not in d1)
