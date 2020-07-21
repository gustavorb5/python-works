bits = input('Enter your byte manually: ')
while bits != "":
    if bits.count('1')+bits.count('0') != 8 or len(bits) != 8:
        print('Wrong byte, try again :(')
    else:
        ones = bits.count('1')
        if ones % 2 == 0:
            print('The parity bit has to be 0')
        else:
            print('The parity bit has to be 1')
    bits = input('Enter your byte manually: ')
