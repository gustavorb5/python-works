day = int(input('Enter a day: '))
month = input('Enter a month: ')
month = month.capitalize()
if day > 0 and day < 32:
    if day < 20 and month == 'March':
        print('The season is winter')
    elif day < 21:
        if month == 'June':
            print('The season is spring')
        elif month == 'December':
            print('The season is fall')
    elif day < 22 and month == 'September':
        print('The season is summer')
    elif day < 30 and month == 'February':
        print('The season is winter')
    elif day < 31:
        if month == 'April':
            print('The season is spring')
        elif month == 'June' and day > 20:
            print('The season is summer')
        elif month == 'November' or (month == 'September' and day > 21):
            print('The season is fall')
        else:
            print('Invalid month')
    elif day < 32:
        if month == 'January' or (month == 'December' and day > 20):
            print('The season is winter')
        elif month == 'May' or (month == 'March' and day >= 20):
            print('The season is spring')
        elif month == 'July' or month == 'August':
            print('The season is summer')
        elif month == 'October':
            print('The season is fall')
        else:
            print('Invalid month')
else:
    print('Invalid date or month')
# wrong code after elif < 32
