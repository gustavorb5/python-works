def properlyDivisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors


def perfectNumber(n):
    perfect_number = False
    if sum(properlyDivisors(n)) == n:
        perfect_number = True
    return perfect_number


for i in range(1, 100000):
    if perfectNumber(i):
        print(i, end=',')
