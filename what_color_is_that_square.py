position = input('Insert a position letter and number: ')
letter = position[0].capitalize()
number = int(position[1])
if letter == 'A' or letter == 'C' or letter == 'E' or letter == 'G':
    if number % 2 == 0:
        print('You\'re in a white square')
    else:
        print('You\'re in a black square')
elif letter == 'B' or letter == 'D' or letter == 'F' or letter == 'H':
    if number % 2 == 0:
        print('You\'re in a black square')
    else:
        print('You\'re in a white square')
