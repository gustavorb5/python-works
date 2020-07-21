month = input('Enter the name of a month: ')
month = month.capitalize()
if month == 'January' or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'October' or month == 'December':
    print(f'{month} has 31 days')
elif month == 'April' or month == 'June' or month == 'September' or month == 'November':
    print(f'{month} has 30 days')
elif month == 'February':
    print(f'{month} could have either 28 or 29 days')
else:
    print('non-existent month')
