age=int(input("Enter your age: "))

years_left = 70-age
days_left = years_left * 365
months_left = years_left * 12
weeks_left = years_left * 52

print(f"You have {days_left} days left, {weeks_left} weeks left, {months_left} months left")
