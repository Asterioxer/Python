set1 = {'Ravi','Golesh','Kalpesh','Shyam'}
set2 = {'Ravi','Kalish','Shyam','Jalesh'}
print(set1.union(set2))
print(set2.union(set1)) #also set1 | set2
set3 = {'Shyam','Arshdeep','Ravi'}
print(set1.union(set2,set3))
print(set1.union(('Mohan','Shyam')))
set1.update(set2)
print(set1)
print(set2.intersection(set1,set3)) #also set1 & set3
set1.intersection_update(set2)
print(set1)
print(set1.difference(set2)) #also set1 - set2
print(set1.difference(('Mokal','Kalop')))
set1.difference_update(set2,set3)
print(set1)
print(set2)
print(set1.symmetric_difference(set2))
print(set1 ^ set2)
set2.symmetric_difference_update(set1)
print(set2)