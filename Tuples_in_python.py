tuple1 = (12,-6,0.98,"Farand",True)
print(type(tuple1[4]))
tuple2 = (45,)
print(tuple1)
print(tuple1[1:4])
print(tuple1[::2])
print(len(tuple1))
tuple3 = (True,"Kalam,0.876,12")
tuple4 = (tuple1,tuple2,tuple3)
tuple5 = (tuple1 + tuple2 + tuple3)
print(tuple4)
print(tuple5)
print(tuple2.count(3))
tuple6 = (10,) * 5
print(tuple6)
