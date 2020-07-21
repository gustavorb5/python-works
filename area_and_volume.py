from math import pi
radius = float(input('Type a radius to calculate area and volume: '))
area = pi * (radius**2)
volume = (4/3*pi) * (radius**3)
print(
    f'Given the radius of {radius}, the area of the sphere is {area} cm2 and the volume is {volume} cm3')
