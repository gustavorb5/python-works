human_age = int(input('Enter your age: '))
if human_age < 0:
    print('Your age cannot be negative')
elif human_age <= 2:
    dog_years = human_age * 10.5
    print(f'Your age in dogs years is {dog_years} years')
else:
    dog_years = (human_age - 2)*4 + 21
    print(f'Your age in dogs years is {dog_years} years')
