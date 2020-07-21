from tabulate import tabulate
temperatures = range(101)
for t in temperatures:
    if t % 10 == 00:
        fahrenheit = (t*(9/5)+32)
        print(tabulate[t, fahrenheit], headers=['Celsius°', 'Fahrenheit'])
