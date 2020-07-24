n = int(input('Enter a number: '))
result = ''
while n != 0:
    remainder = n % 2
    n = int(n/2)
    result += str(remainder)
result = result[::-1]
print(result)
