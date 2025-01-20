def greet(name,subject,dept="CS"):  #default argument should follow non default argument
    print(f"Hi {name}")
    print(f"Do you teach {subject}?")
    print(f"Are you from {dept} department?")

#greet("Jenny","CS","Python") #positional arguments

greet( "Soham", "Python", "My")  #keyword argument = positional argument #positional argument should follow keyword argument

def add(*numbers): #single asterisk is used to accept only arbitrary positional arguments
    c=0
    for i in numbers:
        c = c+i
    print(f"Sum is {c}")
add(5,7,9)
add(18,25,27,39,69,87,86,52,43,22)
