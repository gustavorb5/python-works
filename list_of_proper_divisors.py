def properDivisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors


number = int(input('Enter a number to find out all divisors: '))
for i in properDivisors(number):
    print(i, end=',')
