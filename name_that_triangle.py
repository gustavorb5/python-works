side_1 = float(input('Enter the length of the first side of your triangle: '))
side_2 = float(input('Enter the length of the second side of your triangle: '))
side_3 = float(input('Enter the length of the third side of your triangle: '))
if side_1 == side_2 and side_1 == side_3:
    print('Your triangle is an equilateral one')
elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
    print('Your triangle is an isosceles one')
else:
    print('Your triangle is a scalene one')
