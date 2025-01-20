student_records = {
    "Soham": {"Surname":"Mukherjee", "Gender":"Male", "Prototype":"Sigma", "Influenciability":"Bit"},
    "Sovan": {"Surname":"Khan", "Gender":"Male", "Prototype":"Beta", "Influenciability":"Totally"},
    "Amlan": {"Surname":"Parida", "Gender":"Male", "Prototype":"Lambda", "Influenciability":"Not even a bit to be left behind"},
    "Ashutosh": {"Surname":"Kumar", "Gender":"Male", "Prototype":"Alpha", "Influenciability":"Not even a bit influencable"},
    "Yash": {"Surname":"Sharma", "Gender":"Male", "Prototype":"Ignorant", "Influenciability":"Easily"}
}
print(student_records["Soham"])
student_records["Soham"]["phone_number"]=9065349149
print(student_records["Soham"])
del student_records["Sovan"]["Surname"]
print(student_records["Sovan"])

Provacations = [
    {"Name":"Soham",
     "Gender":"Male",
     "Phone_no":9065349149,
     "Roll_no":2301292114
    },
    {"Name":"Sovan",
     "Gender":"Female",
     "Phone_no":7479297329,
     "Roll_no":2301292420
    },
    {"Name":"Sofen",
     "Gender":"Male",
     "Phone_no":7479243221,
     "Roll_no":2301292840
    }
]
print(Provacations[2])