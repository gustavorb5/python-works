from math import tan, pi
n = int(input('Insert how many sides your polygon has: '))
s = int(input('Insert the length of your sides in cm: '))
area = round((n*(s**2)/4*tan(pi/n)), 3)
print(f'The are of your polygon is {area} cm2')
