student_marks = {
    "Soham" : 98,
    "Donald" : 99,
    "Hermann" : 74,
    "Schwesteiger" : 56,
    "Vervain" : 63,
    "Kandall" : 34,
    "Simpson" : 48,
    "Casper" : 85
}
student_grades = {}
for student in student_marks:
    marks = student_marks[student]
    if marks>90:
        student_grades[student] = "A+"
    elif marks>80:
        student_grades[student] = "A"
    elif marks>70:
        student_grades[student] = "B"
    elif marks>60:
        student_grades[student] = "C"
    elif marks>50:
        student_grades[student] = "D"
    elif marks>40:
        student_grades[student] = "E"
    else:
        student_grades[student] = "F"
    print(student_grades[student])
print(student_grades)