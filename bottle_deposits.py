smaller_container = int(input('How many 1 litre container you have? '))
bigger_container = int(
    input('How many containers of more than 1 litre you have? '))
small = 0.10
big = 0.25
total = smaller_container * small + bigger_container * big
print(f'Your total refund is $ {total}')
