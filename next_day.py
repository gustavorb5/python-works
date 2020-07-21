year = int(input('Enter a year: '))
if year > 0:
    if year % 400 == 0:
        leap_year = True
    elif year % 100 == 0:
        leap_year = False
    elif year % 4 == 0:
        leap_year = True
    else:
        leap_year = False
else:
    print('Non-existent year')
month = int(input('Enter a month: '))
if month in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
    if month in (1, 3, 5, 7, 8, 10, 12):
        month_length = 31
    elif month == 2:
        if leap_year:
            month_length = 29
        else:
            month_length = 28
    else:
        month_length = 30
else:
    print('Non-existent month')
day = int(input('Enter a day: '))
if day > 0 and day <= month_length:
    if day < month_length:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
else:
    print('Non-existent day')
print(f'your next day is {year}-{month}-{day}')
