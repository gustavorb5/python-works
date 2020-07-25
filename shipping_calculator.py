rate = 10.95
rest_rate = 2.95
items = int(input('Enter how many items you purchased: '))


def purchase(x):
    if x > 1:
        final_rate = round(((x-1) * rest_rate) + rate, 2)
    elif x == 1:
        final_rate = rate
    else:
        final_rate = 'Invalid value'
    return final_rate


print(purchase(items))
