regular_price = 3.49
discount = 0.60
purchased_bread = int(
    input('Enter how many loaves of bread you\'ve purchased: '))
initial_price = round(purchased_bread * regular_price, 2)
discount_given = round(initial_price * discount, 2)
total_price = round(initial_price - discount_given, 2)
print(
    f'Your purchase is worth ${initial_price} but due to the fact there\'s a discount of 60 percent in old day bread, your price is ${total_price}')
