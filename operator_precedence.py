def precedence(s):
    if s == "+" or s == "-":
        return 1
    elif s == "*" or s == "/":
        return 2
    elif s == "^":
        return 3
    else:
        return 'INVALID'


operator = input('Enter an operator: ')
a = precedence(operator)
print(a)
