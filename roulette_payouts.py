from random import randrange
number = randrange(0, 38)
if number == 37 or number == 0:
    print('Pay 00')
else:
    print(f'The spin resulted in {number}')
    print(f'Pay {number}')

if number in range(1, 11) or number in range(19, 29):
    if number % 2 == 0:
        color = 'Black'
        print(f'Pay to {color}')
    else:
        color = 'Red'
        print(f'Pay to {color}')
elif number in range(11, 19) or number in range(19, 37):
    if number % 2 == 0:
        color = 'Red'
        print(f'Pay to {color}')
    else:
        color = 'Black'
        print(f'Pay to {color}')
else:
    pass
if number != 0 or number != 37:
    if number % 2 == 0:
        print('Pay Even')
    else:
        print('Pay Odd')
else:
    pass

if number != 0 or number != 37:
    if number >= 1 and number <= 18:
        print('Pay 1 to 18')
    else:
        print('Pay 19 to 36')
else:
    pass
