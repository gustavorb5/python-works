my_money = float(input('How much money have you got into your account?: '))
interest_rate = 0.04 * my_money
total_money_year = round(interest_rate * 12 + my_money, 2)
total_money_year_two, total_money_year_three = round(
    total_money_year * 2, 2), round(total_money_year * 3, 2)
print(f'The total amount of your account after a year is {total_money_year}')
print(
    f'The total amount of your account after two years is {total_money_year_two}')
print(
    f'The total amount of your account after three years is {total_money_year_three}')
