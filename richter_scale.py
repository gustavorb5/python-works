magnitude = float(
    input('Enter a magnitude range of an earthquake in Richter scale: '))
magnitude = round(magnitude, 1)
if magnitude > 0 and magnitude < 2.0:
    earthquake = 'Micro'
elif magnitude >= 2.0 and magnitude < 3.0:
    earthquake = 'Very minor'
elif magnitude >= 3.0 and magnitude < 4.0:
    earthquake = 'Minor'
elif magnitude >= 4.0 and magnitude < 5.0:
    earthquake = 'Light'
elif magnitude >= 5.0 and magnitude < 6.0:
    earthquake = 'Moderate'
elif magnitude >= 6.0 and magnitude < 7.0:
    earthquake = 'Strong'
elif magnitude >= 7.0 and magnitude < 8.0:
    earthquake = 'Major'
elif magnitude >= 8.0 and magnitude < 10.0:
    earthquake = 'Great'
elif magnitude >= 10.0:
    earthquake = 'Meteoric'
else:
    print('Invalid magnitude')
print(f'{magnitude} in Richter scale means that the earthquake is {earthquake}')
