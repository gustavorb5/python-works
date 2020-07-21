r = 8314  # ideal gas constant
t_celsius = float(input('Insert your testing temperature in Celsius: '))
v = float(input('Insert the number of liters that you want to test: '))
p = float(input('Insert the pressure measured in Pascals to test: '))
t_kelvin = t_celsius + 273.15
moles = (p*v) / (r*t_kelvin)
print(f'given {v} liters of a liquid at a pressure of {p} pascals in a room with {t_kelvin} kelvin degrees, we can say the amount of gas is {moles} moles')
