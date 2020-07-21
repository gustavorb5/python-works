banknote = int(input('Enter a banknote value: '))
if banknote == 1:
    figure = 'Geoge Washington'
elif banknote == 2:
    figure = 'Thomas Jefferson'
elif banknote == 5:
    figure = 'Abraham Lincoln'
elif banknote == 10:
    figure = 'Alexander Hamilton'
elif banknote == 20:
    figure = 'Andrew Jackson'
elif banknote == 50:
    figure = 'Ulysses Grant'
elif banknote == 100:
    figure = 'Benjamin Franklin'
else:
    print('Invalid value')
print(f'The figure that appears in the {banknote} dollar bill is {figure}')
