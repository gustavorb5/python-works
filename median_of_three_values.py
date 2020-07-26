num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
num3 = int(input('Enter the last number: '))


def median_value(x, y, z):
    if (x > y and x < z) or (x < y and x > z):
        return x
    elif (y > x and y < z) or (y < x and y > z):
        return y
    elif (z > x and z < y) or (z < x and z > y):
        return z


print(median_value(num1, num2, num3))
