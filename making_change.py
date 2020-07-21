cents_per_toonie = 200
cents_per_loonie = 100
cents_per_quarter = 25
cents_per_dime = 10
cents_per_nickel = 5
value = int(input('Insert the amount of cents you have: '))
toonies = int(value / cents_per_toonie)
cents = int(value % cents_per_toonie)
loonies = int(cents / cents_per_loonie)
cents = int(cents % cents_per_loonie)
quarters = int(cents / cents_per_quarter)
cents = int(cents % cents_per_quarter)
dimes = int(cents / cents_per_dime)
cents = int(cents % cents_per_dime)
nickels = int(cents / cents_per_nickel)
cents = int(cents % cents_per_nickel)
print(f'Your change for {value} cents: is {toonies} toonies coins, {loonies} loonies coins, {quarters} quarters coins, {dimes} dimes coins, {nickels} nickels coins and {cents} cents coins')
