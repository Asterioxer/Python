namelm = input("Enter the name of the male lover ")
namelf = input("Enter the name of the female lover ")
combine_names = namelm + namelf
lower_case_name = combine_names.lower()

t = lower_case_name.count('t')
r = lower_case_name.count('r')
u = lower_case_name.count('u')
e = lower_case_name.count('e')
true = t + r + u + e

l = lower_case_name.count('l')
o = lower_case_name.count('o')
v = lower_case_name.count('v')
e = lower_case_name.count('e')
love = l + o + v + e

love_scales = int(str(true) + str(love))
if love_scales < 10 or love_scales > 90: 
    print(f"Your scaling is {love_scales} and you go like Coke and Mentos")
elif love_scales >= 40 and love_scales <= 50:
    print(f"Your scaling is {love_scales} and you are alright")
else:
    print(f"Your love scaling is {love_scales}")