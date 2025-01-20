# this program lays emphasis on the aspects of retrun statements and how multiple return values and given
import statistics
def mean_median_mode(list1):
    return [statistics.mean(list1),statistics.median(list1),statistics.mode(list1)] #anything written after this return statement would be ignored


# print(mean_median_mode([3,5,46,74,89,1,97,1,46,1])) #one way
'''result = mean_median_mode([3,5,46,74,89,1,97,1,46,1])
print(result)''' #another way
a,b,c = mean_median_mode([3,5,46,74,89,1,97,1,46,1])
print(f"Mean is {a}, Median is {b}, Mode is {c}") #third way

def add(a,b):
    if a==0 and b==0:
        return      #this shows that whenever 0 is taken for both a and b a {None} is returned by default in the output if nothing's mentioned after return
    else:
        return a+b
    
var1 = int(input("Enter first variable:\n"))
var2 = int(input("Enter second variable:\n"))
result_is = add(var1,var2)
print(f"the result is {result_is}") 