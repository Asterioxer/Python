'''def func_name(parameters):  #general syntax
    func_body #c=a+b
    return c'''#return is a special function only used within a function

def add(a,b):
    c = a+b
    return c

result = add(23,65)
print(result)

def format_name(f_name,l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name("Soham","Mukherjee"))
