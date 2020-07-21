user1 = int(input('Enter a value: '))
user2 = int(input('Enter another value: '))
user3 = int(input('And enter the last value: '))
min_value = min(user1, user2, user3)
max_value = max(user1, user2, user3)
middle_value = user1 + user2 + user3 - min_value - max_value
print(
    f'Given your three numbers, the max one is {max_value}, the min one {min_value} and the middle one is {middle_value}')
