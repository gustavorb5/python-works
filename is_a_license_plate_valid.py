plate = input('Enter a license plate: ')
plate = plate.upper()
if len(plate) == 6 and (plate[0], plate[1], plate[2] >= 'A' and plate[0], plate[1], plate[2] <= 'Z') \
        and (plate[3], plate[4], plate[5] >= '0' and plate[3], plate[4], plate[5] <= '9'):
    valid_plate = True
elif len(plate) == 7 and (plate[0], plate[1], plate[2], plate[3] >= '0' and plate[0], plate[1], plate[2], plate[3] <= '9') \
        and (plate[4], plate[5], plate[6] >= 'A' and plate[4], plate[5], plate[6] <= 'Z'):
    valid_plate = True
else:
    valid_plate = False
if valid_plate:
    if len(plate) == 6:
        print(f'Your plate {plate} is an old one')
    else:
        print(f'Your plate {plate} is a new one')
else:
    print('Invalid plate')
