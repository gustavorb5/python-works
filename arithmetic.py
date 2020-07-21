from math import log10
a = int(input('Type your first number: '))
b = int(input('Type your second number: '))
sm = a + b
dif = a - b
prt = a*b
qtn = round(a / b)
rmd = a % b
lg = round(log10(a))
pw = a**b
print(sm, dif, prt, qtn, rmd, lg, pw)
