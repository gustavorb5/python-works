kilopascal_pressure = int(input('Enter a pressure level in kPa: '))
pounds_per_square_inch = kilopascal_pressure / 6.895
millimeters_of_mercury = kilopascal_pressure * 7501
atmospheres = kilopascal_pressure / 101
print(f'Your {kilopascal_pressure} kPa of pressure is equal to {pounds_per_square_inch} psi, {millimeters_of_mercury} mm Hg and {atmospheres} atm')
