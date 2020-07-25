base = 4
meters = 140
cost_per_distance = 0.25
distance = float(input('Type how long was the travel in km: '))


def travel(x):
    conversion = distance * 1000
    cost = (conversion / meters) * cost_per_distance
    total = round(base + cost, 2)
    return total


print(f'your trip costs ${travel(distance)}')
