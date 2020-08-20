from days_in_a_month import daysMonth


def magicDates(m, d, y):
    magic_date = False
    if m * d == y % 100:
        magic_date = True
    return magic_date


for i in range(1900, 2000):
    for j in range(1, 13):
        for k in range(1, daysMonth(i, j)+1):
            if magicDates(j, k, i):
                print(f'{j}-{k}-{i} is a magic date')
# la concha tuya porque no puedo importar funcioneeeeeeeeeeeeeeeeeeeeeeeeeeeeeees
