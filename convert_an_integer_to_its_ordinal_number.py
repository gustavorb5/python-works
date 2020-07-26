number = int(input('Enter a number 1-12: '))
ordinal = ''


def ordinal_number(x):
    if x == 1:
        ordinal = 'First'
    elif x == 2:
        ordinal = 'Second'
    elif x == 3:
        ordinal = 'Third'
    elif x == 4:
        ordinal = 'Fourth'
    elif x == 5:
        ordinal = 'Fifth'
    elif x == 6:
        ordinal = 'Sixth'
    elif x == 7:
        ordinal = 'Seventh'
    elif x == 8:
        ordinal = 'Eighth'
    elif x == 9:
        ordinal = 'Ninth'
    elif x == 10:
        ordinal = 'Tenth'
    elif x == 11:
        ordinal = 'Eleventh'
    elif x == 12:
        ordinal = 'Twelfth'
    else:
        ordinal = 'Number no found'
    return ordinal


print(ordinal_number(number))
