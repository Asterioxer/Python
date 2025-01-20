numbers = [10,0,-3,7,6]
names = ['Jango' , "Kalvin" , 'Lethargy']
mix_list = [1 , "Germanium" , True , 19.0876]
print(numbers)
print(names)
print(mix_list)

print(len(numbers))
print(numbers[-1])
print(numbers[3])

print(numbers[0:5])
print(numbers[1:4])

#list functions
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

print(min(numbers))

print(max(numbers))

numbers.append(45)
print(numbers)

numbers.insert(1,78)
print(numbers)

numbers.extend([67,98,54,34])
print(numbers)

numbers.remove(10)
print(numbers)

print(numbers.pop(5)) #returns the value that was popped out
print(numbers)

numbers[1:4]=[45,46,67] #modify elments in the list
print(numbers)

print(numbers.count(67))
