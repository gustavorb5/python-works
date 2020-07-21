water_heat_capacity = 4186
electricity_cost = 8.9
mass = float(input('Enter an amount of mass: '))
temperature = float(input('Insert a temperature: '))
q = mass * temperature * water_heat_capacity
kwh = q / 3.6e+6
cost = kwh * electricity_cost
print(
    f'The amount of energy required to heat {mass} grams by {temperature} degree celsius is {q} and it costs {cost} cents')
