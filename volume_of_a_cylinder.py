from math import pi
radius = int(input('Insert the radius of the base of the cylinder: '))
height = int(input('Type the height of your cylinder: '))
volume = round(pi * (radius**2) * height, 2)
print(f'The volume of your cylinder is {volume} cm3')
