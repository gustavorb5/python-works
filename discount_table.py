discount = 0.60
price_list = [4.95, 9.95, 14.95, 19.95, 24.95]
for price in price_list:
    total = round(price - (discount*price), 2)
    print(
        f'Your product costs ${price}, but with the discount now it\'s only ${total}')
