from math import sqrt
side1 = int(input('Type the first side of the triangle in cm: '))
side2 = int(input('Type the second side of the triangle in cm: '))
side3 = int(input('Type the third side of the triangle in cm: '))
s = (side1 + side2 + side3)/2
area = round(sqrt(s * (s - side1)*(s-side2)*(s-side3)), 2)
print(f'The area of the triangle is {area} cm2')
