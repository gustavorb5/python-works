from math import cos, acos, sin, asin, tan, atan, degrees, radians
latitude_1 = float(input('Type the latitude of your first point: '))
latitude_2 = float(input('Type the latitude of your second point: '))
longitude_1 = float(input('Type the longitude of your first point: '))
longitude_2 = float(input('Type the longitude of your second point: '))
distance = 6371.01 * acos(sin(latitude_1)*sin(latitude_2) +
                          cos(latitude_1)*cos(latitude_2)*cos(longitude_1-longitude_2))
print(
    f'The distance between point A {latitude_1},{longitude_1} and point B {latitude_2},{longitude_2} is {distance} kilometers')
