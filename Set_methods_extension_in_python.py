set1 = {1,3,4,6,9}
set2 = {1,3,4,6,9}
print(set1.isdisjoint(set2))
set3 = {2,5,7,8}
print(set3.isdisjoint(set1))
print(set1.issubset(set2))
print(set1 <= set1)
print(set2.issuperset(set1))
print(set1 >= set3)
set2.clear()
print(set2)