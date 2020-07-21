# exercise 55
frequency = float(input('Enter a frequency in Hz: '))
if frequency > 0 and frequency < 3e+9:
    name = 'Radiowaves'
elif frequency >= 3e+9 and frequency < 3e+12:
    name = 'Microwaves'
elif frequency >= 3e+12 and frequency < 4.3e+14:
    name = 'Infrared light'
elif frequency >= 4.3e+14 and frequency < 7.5e+14:
    name = 'Visible light'
elif frequency >= 7.5e+14 and frequency < 3e+17:
    name = 'Ultraviolet light'
elif frequency >= 3e+17 and frequency < 3e+19:
    name = 'X-rays'
elif frequency >= 3e+19:
    name = 'Gamma'
else:
    name = 'Non-Existent'

if name == 'Non-Existent':
    print('Invalid range of frequency.')
else:
    print(
        f'Due to its frequency of {frequency}, your electromagnetic radiation is {name}')
