month = input('Enter a month: ').capitalize()
day = int(input('Enter a day: '))
if month == 'January' and day == 1:
    print('Happy new year!')
elif month == 'December' and day == 25:
    print('Merry Christmas everybody')
elif month == 'July' and day == 1:
    print('Happy Canada\'s day to all')
else:
    print('Invalid date')
