user = int(input('Enter a 4-digit number: '))
first = int(user / 1000)
remainder = int(user % 1000)
second = int(remainder / 100)
remainder = int(remainder % 100)
third = int(remainder/10)
remainder = int(remainder % 10)
sum = first + second + third + remainder
print(
    f'The sums of the digit of the number {user} is {sum} ({first} + {second} + {third} + {remainder})')
