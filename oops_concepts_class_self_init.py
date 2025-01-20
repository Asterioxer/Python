class Instructor:
    def __init__(self,instructor_name,affinity,instagram_followers):
        self.name = instructor_name
        self.affinity = affinity
        self.followers=instagram_followers

instructor_1 = Instructor("Soham","Ranchi","5 Mil.")
print(instructor_1.name)
print(instructor_1.affinity)
print(instructor_1.followers)

def __init__(self): #init method is used to initialize data members of a class while creating an object
    print("Creating a new object")
      
    #pass

#instructor_1 = Instructor()  #object of the instructor class
#instructor_1.name = "Payal"  #accessing it
#instructor_1.address = "Delhi"  #similar to here
#print(instructor_1.name)
#ins_2 = Instructor()
#ins_2.name = "Soham"
#ins_2.address = "BKB"
#print(ins_2.name) 

#constructor assigns/initializes value to the data members when an object is created


#create 2 more instructors pass name and address as well as print them.



class Intruder:    #i am creating these two with a base name of inturuders
    def __init__(self,name_2, address_2):
        self.name = name_2
        self.address = address_2

intruder_1 = Intruder("Anjaan", "Baharagora,Odisha")
intruder_2 = Intruder("Ajay", "Darbhanga,Bihar")

print(intruder_1.name)
print(intruder_1.address)
print(intruder_2.name)
print(intruder_2.address)