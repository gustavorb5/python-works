year = int(input('Enter a year: '))
if year % 12 == 8:
    zodiac_animal = 'Dragon'
elif year % 12 == 9:
    zodiac_animal = 'Snake'
elif year % 12 == 10:
    zodiac_animal = 'Horse'
elif year % 12 == 11:
    zodiac_animal = 'Sheep'
elif year % 12 == 0:
    zodiac_animal == 'Monkey'
elif year % 12 == 1:
    zodiac_animal = 'Rooster'
elif year % 12 == 2:
    zodiac_animal = 'Dog'
elif year % 12 == 3:
    zodiac_animal = 'Pig'
elif year % 12 == 4:
    zodiac_animal = 'Rat'
elif year % 12 == 5:
    zodiac_animal = 'Ox'
elif year % 12 == 6:
    zodiac_animal = 'Tiger'
elif year % 12 == 7:
    zodiac_animal = 'Hare'
else:
    print('Invalid year')

print(f'The zodiac animal of {year} is {zodiac_animal}')
