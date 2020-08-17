def checkingPassword(a):
    checker1 = False
    checker2 = False
    checker3 = False
    for i in a:
        if i.isupper():
            checker1 = True
            # break
        if i.islower():
            checker2 = True
            # break
        if i.isdigit():
            checker3 = True
            # break
    if checker1 and checker2 and checker3:
        return True
    else:
        return False


password = input('Enter a password: ')
print(checkingPassword(password))
