word = input('Enter a word: ')
width = int(input('Enter a number: '))


def centralizacion(word, width):
    if width < len(word):
        return word
    else:
        result = (width - len(word)) // 2
        b_spaces = ':)' * result
        final_string = b_spaces + word + b_spaces
        print(len(final_string))
        return final_string


print(centralizacion(word, width))
