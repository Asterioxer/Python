list1 = ["hi","Hello","Welcome"]
names = ["Krishna","Ram","Madhav"]
for item in list1:
    for name in names:
        print(item,name)
        if item=="hello" and name=="Ram":
            break
        print("Out from inner loop")
print("out of outer loop")