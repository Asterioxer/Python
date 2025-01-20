import random

a = random.randint(1,10)
print(a)

b = random.randrange(1,4)
print(b)

c = random.random()
print(c)

d = random.uniform(1,4)
print(d)

l = [2 , -54 , 0 , 98 , -43]
e = random.choice(l)
print(e)

n = [23,45,-23,56,43]
random.shuffle(n)
print(n)