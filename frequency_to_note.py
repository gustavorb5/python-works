freq = float(input('Enter a frequency level in hz: '))
if freq == 261.63:
    print('Your note is C4')
elif freq == 293.66:
    print('Your note is D4')
elif freq == 329.63:
    print('Your note is E4')
elif freq == 349.23:
    print('Your note is F4')
elif freq == 392.00:
    print('Your note is G4')
elif freq == 440.00:
    print('Your note is A4')
elif freq == 493.88:
    print('Your note is B4')
else:
    print('invalid frequency')
