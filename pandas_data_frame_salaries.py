import pandas as pd
import numpy as np

def ca_sal(ba_sal):
    TA = 0.01 * ba_sal
    DA = 0.08 * ba_sal
    HRA = 0.15 * ba_sal
    gross_sal = ba_sal + TA + DA + HRA
    return gross_sal

n_emp = int(input("Enter number of employees: "))

names = []
dojs = []
ba_salary = []
tas = []
das = []
hras = []
grss = []

for i in range(n_emp):
    name = input(f"Enter name of employee {i+1}: ")
    doj = input(f"Enter date of joining {i+1} (DD-MM-YYYY): ")
    ba_salary = float(input(f"Enter basic salary of employee {i+1}: "))

TA, DA, HRA, gross_sal = ca_sal(ba_sal)

names.append(name)


