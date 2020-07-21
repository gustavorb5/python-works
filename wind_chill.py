# i choose these names because i don't really know what they represent in the formula
first_value = 13.12
second_value = 0.6215
third_value = 11.37
fourth_value = 0.3965
exponent = 0.16
t = float(input('Enter the temperature in Celsius degree: '))
v = float(input('Enter the speed of the wind in km/h: '))
wci = int(first_value + second_value*t - third_value *
          (v**exponent) + fourth_value*t*(v**exponent))
print(f'The wind chill index is {wci}')
