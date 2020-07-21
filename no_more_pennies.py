price = float(input('Enter the price of the product: '))
total = 0
while price >= 0:
    total = total + price
    price = float(input('Enter the price of the product: '))
option = input('Would you pay with cash or by credit card?: ')
option = option.capitalize()
if option == 'Cash':
    rounder = total * 100 % 5
    if rounder > 2.5:
        cash_total = total - rounder/100
        print(f'You have to pay ${cash_total}')
    else:
        cash_total = total + 0.05 + rounder/100
        print(f'You have to pay ${cash_total}')
elif option == 'Card':
    print(f'You have to pay ${total}')
else:
    print('Invalid payment method')
