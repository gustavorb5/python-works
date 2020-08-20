def measure(n, unit):
    unit = unit.lower()
    if unit == 'cups' or unit == 'cup':
        teaspoons = n*48
    elif unit == 'tablespoon' or unit == 'tablespoons':
        teaspoons = n*3
    elif unit == 'teaspoon' or unit == 'teaspoons':
        teaspoons = n
    cups = teaspoons // 48
    teaspoons = teaspoons % 48
    tablespoons = teaspoons // 3
    teaspoons = teaspoons % 3
    result = ''
    if cups:
        result = f'{cups} cup'
        if cups > 1:
            result += 's'
    if tablespoons:
        if result != '':
            result += ', '
        result += f'{tablespoons} tablespoon'
        if tablespoons > 1:
            result += 's'
    if teaspoons:
        if result != '':
            result += ' and '
        result += f'{teaspoons} teaspoon'
        if teaspoons > 1:
            result += 's'
    return result


unit_measure = input('Enter the unity of measure: ')
amount_measure = int(input('Enter the amount of measure: '))

print(f'You will need {measure(amount_measure, unit_measure)}')
