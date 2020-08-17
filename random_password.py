from random import randint


def generatePassword():
    password_generate = ""
    pass_length = randint(7, 10)
    for i in range(pass_length):
        character = chr(randint(33, 126))
        password_generate += character
    return password_generate


password = generatePassword()
print(password)
