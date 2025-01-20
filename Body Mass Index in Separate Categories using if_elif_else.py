weight = float(input('Enter Weight in Kg: '))
height = float(input('Enter Height in Meter: '))

BMI = round(weight/height ** 2)

if BMI < 16.0:
    print(f"Underweight (Severe thinness) with {BMI}")
elif BMI >= 16.0 and BMI <= 16.9:
    print(f"Underweight (Moderate thinness) with {BMI}")
elif BMI > 17.0 and BMI <= 18.4:
    print(f"Underweight (Mild thinness) with {BMI}")
elif BMI >= 18.5 and BMI <= 24.9:
    print(f"Healthy Weight Range with {BMI}")
elif BMI >= 25.0 and BMI <= 29.9:
    print(f"Overweight (Pre-Obese class) with {BMI}")
elif BMI >= 30.0 and BMI <= 34.9:
    print(f"Obese (Class I) with {BMI}")
elif BMI >= 35.0 and BMI  <=39.9:
    print(f"Obese (Class II) with {BMI}")
else:
    print(f"Obese (Class III and above) with {BMI}")