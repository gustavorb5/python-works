height = float(input('Insert your height in meters, not centimeters: '))
weight = float(input('Enter your weight in kilograms: '))
bmi = round(weight / (height**2), 2)
print(
    f'being your height {height} m and {weight} kg your weight, your BMI is {bmi}')
