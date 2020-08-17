def primeNumber(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
        return True


number = int(input('Enter a number: '))
if primeNumber(number):
    print('Your number is prime')
else:
    print('Your number is not prime')
