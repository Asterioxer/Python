heights = input("Enter the heights separated by space: ")
height_list = heights.split()
count=0
for height in height_list:
    count =count+1
print(count)
for i in range(0,count):
    height_list[i]=int(height_list[i])

sum=0
for person in height_list:
    sum += person
avg = sum/count
print(avg)
    