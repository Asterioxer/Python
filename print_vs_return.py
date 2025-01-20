'''def func1(a,b):
    c = a+b
    print(c)
op1 = func1(3,4)
print(op1)

def func2(a,b):
    c = a+b
    return c
op2 = func2(3,4)
print(op2)'''

def func1(x):
    return x+1

def func2(a,b):
    c = a+b
    return c
op2 = func2(3,4)
final_op = func1(op2)
print(final_op)