student_data = [
    {
        "Name":"Soham",
        "Roll_no":114,
        "Age":20,
        "Course":"CSE"
    },
    {
        "Name":"Ranjan",
        "Roll_no":128,
        "Age":22,
        "Course":"B.Sc"
    }
]

def add_new_student(name,roll_no,age,course):
    new_student = {}
    new_student["Name"] = name
    new_student["Roll_no"] = roll_no
    new_student["Age"] = age
    new_student["Course"] = course 
    student_data.append(new_student)

add_new_student("Somesh",125,25,"B.C.A.")
print(student_data)