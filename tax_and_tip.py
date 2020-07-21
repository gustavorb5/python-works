price = int(input('Type the cost of your meal without tax and tip: '))
tax = price * 0.21
tip = price * 0.10
total = price + tax + tip
print(f'The cost of your meal, with tax and tip added is $ {total}')
