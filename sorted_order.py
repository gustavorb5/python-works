numbers_list = []
number = int(input('Start typing numbers... type 0 to finish: '))
while number != 0:
    numbers_list.append(number)
    number = int(input('Start typing numbers... type 0 to finish: '))
for i in numbers_list:
    print(i, end='')
