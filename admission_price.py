total = 0
welcome = input(
    'Welcome to Gusty\'s Zoo. As part of a group, please indicate the age of each individual of the group: ')
while welcome != "":
    welcome = int(welcome)
    if welcome <= 2 and welcome > 0:
        total += 0
    elif welcome > 2 and welcome <= 12:
        total += 14.00
    elif welcome > 65:
        total += 18.00
    else:
        total += 23.00
    welcome = input(
        'Welcome to Gusty\'s Zoo. As part of a group, please indicate the age of each individual of the group: ')
total = round(total, 2)
print(f'The price for the group is ${total}')
# comment to check git
