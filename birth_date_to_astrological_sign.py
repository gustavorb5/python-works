month = input('Enter your birth month: ')
month = month.capitalize()
day = int(input('Enter your birthday: '))
if (month == 'December' and (day > 21 and day < 32)) or (month == 'January' and (day > 0 and day < 20)):
    print('Your sign is Capricorn')
elif (month == 'January' and (day > 19 and day < 32)) or (month == 'February' and (day > 0 and day < 19)):
    print('Your sign is Aquarius')
elif (month == 'February' and (day > 18 and day < 30)) or (month == 'March' and (day > 0 and day < 21)):
    print('Your sign is Pisces')
elif (month == 'March' and (day > 20 and day < 32)) or (month == 'April' and (day > 0 and day < 20)):
    print('Your sign is Aries')
elif (month == 'April' and (day > 19 and day < 31)) or (month == 'May' and (day > 0 and day < 21)):
    print('Your sign is Taurus')
elif (month == 'May' and (day > 20 and day < 32)) or (month == 'June' and (day > 0 and day < 21)):
    print('Your sign is Gemini')
elif (month == 'June' and (day > 20 and day < 31)) or (month == 'July' and (day > 0 and day < 23)):
    print('Your sign is Cancer')
elif (month == 'July' and (day > 22 and day < 32)) or (month == 'August' and (day > 0 and day < 23)):
    print('Your sign is Leo')
elif (month == 'August' and (day > 22 and day < 32)) or (month == 'September' and (day > 0 and day < 23)):
    print('Your sign is Virgo')
elif (month == 'September' and (day > 22 and day < 31)) or (month == 'October' and (day > 0 and day < 23)):
    print('Your sign is Libra')
elif (month == 'October' and (day > 22 and day < 32)) or (month == 'November' and (day > 0 and day < 22)):
    print('Your sign is Scorpio')
elif (month == 'November' and (day > 21 and day < 31)) or (month == 'December' and (day > 0 and day < 22)):
    print('Your sign is Sagitarius')
else:
    print('Invalid month or day')
