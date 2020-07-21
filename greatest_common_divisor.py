num1 = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))
while num1 % num2 != 0:
    num2 = num1 % num2
    gcd = num1 % num2
if gcd == 0:
    print(f'{num2} is the GCD')
# me vuelvo locooooooooo me salioooooo
