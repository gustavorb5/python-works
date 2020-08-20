positives = []
negatives = []
zeros = []
num = input('Start typing numbers, enter to exit: ')
while num != '':
    number = int(num)
    if number > 0:
        positives.append(number)
    elif number < 0:
        negatives.append(number)
    else:
        zeros.append(number)
    num = input('Start typing numbers, enter to exit: ')
for i in positives, negatives, zeros:
    print(i, end='')
