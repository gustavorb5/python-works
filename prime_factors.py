num = int(input('Enter a number: '))
factor = 2
print(f'prime factors of {num} are: ')
while factor <= num:
    if num % factor == 0:
        print(f'{factor}')
        num = int(num / factor)
    else:
        factor += 1
