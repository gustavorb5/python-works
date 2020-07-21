wavelength = int(input('Enter a wavelength in nm: '))
if wavelength >= 380 and wavelength < 450:
    color = 'Violet'
elif wavelength >= 450 and wavelength < 495:
    color = 'Blue'
elif wavelength >= 495 and wavelength < 570:
    color = 'Green'
elif wavelength >= 570 and wavelength < 590:
    color = 'Yellow'
elif wavelength >= 590 and wavelength < 620:
    color = 'Orange'
elif wavelength >= 620 and wavelength < 750:
    color = 'Red'
else:
    color = 'No avalaible'
print(f'The wavelength of {wavelength} nm. is {color}')
