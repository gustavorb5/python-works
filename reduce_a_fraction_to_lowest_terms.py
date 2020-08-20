def getGcd(a, b):
    while b:
        a, b = b, a % b
    return a


def simplifyFraction(a, b):
    num = int(a / getGcd(a, b))
    den = int(b / getGcd(a, b))
    return f'Your original fraction {a}/{b} was reduced to {num}/{den}'


number1 = int(input('Enter numerator: '))
number2 = int(input('Enter denominator: '))
print(simplifyFraction(number1, number2))
