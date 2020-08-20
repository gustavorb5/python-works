numbers = []
num = int(input('Enter a number, press 0 to stop: '))
while num != 0:
    numbers.append(num)
    num = int(input('Enter a number, press 0 to stop: '))
numbers.reverse()
for i in numbers:
    print(i)
