binary = input('Enter a binary number: ')
exp = 0
decimal = 0
for i in binary:
    n = int(i)
    conv = n * (2**exp)
    decimal += conv
    exp += 1
print(decimal)
