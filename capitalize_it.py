phrase = input(
    'Enter a phrase or something, don\'t worry about capital letters ;) : ')


def capitalizeWords(ph):
    result = ph.replace(" i ", " I ")
    if len(ph) > 0:
        result = result[0].upper() + result[1:len(result)]
    position = 0
    while position < len(ph):
        if result[position] == "!" or result[position] == "?" or result[position] == ".":
            position += 1
            while position < len(ph) and result[position] == " ":
                position += 1
            if position < len(ph):
                result = result[0:position] + result[position].upper() + \
                    result[position + 1: len(result)]
        position += 1
    return result


print(capitalizeWords(phrase))
