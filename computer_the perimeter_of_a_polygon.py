from math import sqrt
perimeter = 0
x_first = float(input('Enter the x of the coordinate: '))
y_first = float(input('Enter the y of the coordinate: '))
prev_x = x_first
prev_y = y_first
# we do this way to transform "" into a conditional value
number_x = input('Enter the x of the coordinate: ')
while number_x != "":
    x = float(number_x)
    y = float(input('Enter the y of the coordinate: '))
    distance = sqrt((x - prev_x)**2 + (y - prev_y)**2)
    perimeter = perimeter + distance
    prev_x = x
    prev_y = y
    number_x = input('Enter the x of the coordinate: ')
distance = sqrt((x - x_first)**2 + (y - y_first)**2)
perimeter = round(perimeter + distance, 4)
print(f'The perimeter of your polygon is {perimeter} cm.')
