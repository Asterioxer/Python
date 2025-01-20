def add(*numbers,name): #args->arbitrary arguments
    c=0
    print(numbers)
    print(name)
    for i in numbers:
        c += i 
    print(f"Sum is {c}")

add(2,5,9,name="Soham")

def info_person(*args,**kwargs): #kwargs->keyworded arguments
    for key,value in kwargs.items():
        print(key,value)
    print(args)
info_person(1,2,name="Ram",age=30,dept="CSE")
info_person(1,2,3,name="Shyam",dept="CSE")