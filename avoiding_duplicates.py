names = []
name = input('Start typing names, press enter to cancel: ')
while name:
    names.append(name)
    name = input('Start typing names, press enter to cancel: ')
names = set(names)
for i in names:
    print(i)
