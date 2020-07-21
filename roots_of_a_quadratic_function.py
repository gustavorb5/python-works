from math import sqrt
a = int(input('Enter a value: '))
b = int(input('Enter a value: '))
c = int(input('Enter a value: '))
square_root = b**2 - 4*a*c
if square_root > 0:
    x1 = ((-(b) + sqrt(square_root))/2*a)
    x2 = ((-(b) - sqrt(square_root))/2*a)
    print(f'The roots are {x1} and {x2}')
elif square_root == 0:
    x = -(b)/(2*a)
    print(f'The root is {x}')
else:
    print('No roots for this function')
