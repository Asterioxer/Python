set1 = {21,9.56,'Gallery',True,True,1}
print(set1)
set2 = {23,65,7.8,"Frankenstein",True,75,64}
set3 = ()
print(type(set1))
print(type(set2))
print(type(set3))
set1.add(99)
print(set1)
set1.remove(21)
print(set1)
set2.discard("Frankenstein")
print(set2)