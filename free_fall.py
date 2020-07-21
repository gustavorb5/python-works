from math import sqrt
a = 9.8  # acceleration 9.8 per squared second
vi = 0  # initial speed when an object is dropped
# d for distance
d = float(input('Insert the height of where you want to drop an object: '))
vf = round(sqrt(vi**2 + 2*a*d), 2)  # vf for final speed
print(f'your object will fall at {vf}m/s2')
