counter = 0
total = 0
n = int(input('Enter a number: '))
while n != 0:
    if n != 0:
        counter += 1
        total += n
        n = int(input('Enter a number: '))
if counter != 0:
    average = total / counter
    print(f'The average is {average}')
else:
    print('NOOOOOOO you just can\'t start the loop with 0, that will break the program')
    print('HAHA, 0 goes crash crash')
