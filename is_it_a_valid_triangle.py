side1 = int(input('Enter the length of the first side: '))
side2 = int(input('Enter the length of the second side: '))
side3 = int(input('Enter the length of the third side: '))
print('It\'s a triangle?')


def checkingTriangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    else:
        return True


print(checkingTriangle(side1, side2, side3))
