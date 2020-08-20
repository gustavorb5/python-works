def daysMonth(m, x):
    leap_year = False
    days = 0
    if m % 4 == 0:
        if m % 100 == 0:
            if m % 400 == 0:
                leap_year = True
        else:
            leap_year = True

    if x >= 1 and x <= 12:
        if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
            days = 31
        elif x == 2:
            days = 28
            if leap_year:
                days = 29
        else:
            days = 30
    return days


month = int(input('Enter a month: '))
year = int(input('Enter the year: '))
print(
    f'That month had {daysMonth(year, month)} days')
