x = int(input('Enter a number: '))
y = int(input('Enter a number: '))


def something(a, b):
    while b:
        a, b = b, a % b
    return a


# me vuelvo locooooooooo me salioooooo
print(something(x, y))
