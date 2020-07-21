shape_number = int(input('Enter how many sides has your shape: '))
if shape_number >= 3 and shape_number <= 10:
    if shape_number == 3:
        print('Your shape is a triangle.')
    elif shape_number == 4:
        print('Your shape is a square.')
    elif shape_number == 5:
        print('Your shape is a pentagon.')
    elif shape_number == 6:
        print('Your shape is a hexagon.')
    elif shape_number == 7:
        print('Your shape is a heptagon.')
    elif shape_number == 8:
        print('Your shape is an octagon.')
    elif shape_number == 9:
        print('Your shape is a nonagon.')
    else:
        print('Your shape is a decagon.')
else:
    print('Inappropiate number of sides.')
