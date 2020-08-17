def isInteger(s):
    s = s.strip()
    if (s[0] == "+" or s[0] == "-") and s[1:].isdigit():
        return True
    else:
        return False


phrase = input('Enter a phrase: ')
if isInteger(phrase):
    print('The phrase represents and integer')
else:
    print('Type well you idiot')
