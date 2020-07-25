from random import randint
max_number = randint(0, 100)
counting = 0
print(f'{max_number} is the first max value')
for i in range(100):
    i = randint(1, 100)
    print(i)
    if i > max_number:
        max_number = i
        print(f'{max_number} update')
        counting += 1
print(f'{max_number} is the max value')
print(f'and the max value was updated {counting} many times')
