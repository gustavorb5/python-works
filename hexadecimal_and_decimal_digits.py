def hex2int(a):
    if a >= '0' and a <= '9':
        a = int(a)
        return a
    elif a >= 'A' and a >= 'F':  # i dont understand this linea, if i fix it, it doesnt work anymore
        a = a.upper()
        if a == 'A':
            a = 10
        elif a == 'B':
            a = 11
        elif a == 'C':
            a = 12
        elif a == 'D':
            a = 13
        elif a == 'E':
            a = 14
        elif a == 'F':
            a = 15
    return a


def int2hex(a):
    if a >= 0 and a <= 9:
        a = str(a)
        return a
    elif a >= 10 and a <= 15:
        if a == 10:
            a = 'A'
        elif a == 11:
            a = 'B'
        elif a == 12:
            a = 'C'
        elif a == 13:
            a = 'D'
        elif a == 14:
            a = 'E'
        elif a == 15:
            a = 'F'
        return a


choice = int(
    input('Enter 1 to convert from hex to dec, 2 to convert from dec to hex: '))
if choice == 1:
    choice = input('Enter an hex value to convert: ')
    print(hex2int(choice))
elif choice == 2:
    choice = int(input('Enter a dec value to convert: '))
    print(int2hex(choice))
