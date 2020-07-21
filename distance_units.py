feet = int(input('Insert a longitude in feet: '))
inch = 12 * feet
yard = inch / 36
mile = yard / 1760
print(
    f'your longitude is {feet} feet long, {inch} inches long, {yard} yards long and {mile} miles long')
