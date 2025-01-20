class Bike:
    name = ""
    gear = 0

bike1 = Bike()
bike1.gear = 8
bike1.name = "Pulsar"
print(f"The bike name is: {bike1.name}, the gears are: {bike1.gear}")  #Class and object normal program




#Public class
class MyClass:
    def __init__(self):
     self.public_var = 10
obj = MyClass()
print(obj.public_var)  #accessing the public variable

#Private class
class MypClass:
    def __init__(self):
        self.__private_var = 20
obp = MypClass()
print(obp.__private_var) #accessing the private variable this results into an attribute error


#Protected class
class MyppClass:
   def __init__(self):
      self._protected_variable = 30

class SubppClass(MyppClass):
   def d_pro(self):
      print(self._protected_variable)

obpp = SubppClass()
obpp.d_pro() #accessing the protected variable this results into an attribute error


#Encapsulation
class Mclass:
   def __init__(self):
      self.__private_var = 202

   def get_private_variable(self):
      return self.__private_var
   
   def set_private_variable(self, value):
      if value > 0:
         self.__private_var = value

objp = Mclass()
print(objp.get_private_variable()) #accessing the private variable using getter

objp.set_private_variable(100) #modifying the private member using setter
