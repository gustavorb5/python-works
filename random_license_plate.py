from random import randint


def generatePlate():
    plate = ""
    for i in range(4):
        character = chr(randint(48, 57))
        #character = str(character)
        plate += character
    for i in range(3):
        character = chr(randint(65, 90))
        plate += character
    return plate


new_plate = generatePlate()
print(new_plate)
