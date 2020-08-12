from convert_an_integer_to_its_ordinal_number import ordinal_number


def verse(num):
    return f'On the {ordinal_number(num)} day of christmas my true love sent to me: '
    if num >= 12:
        return 'twelve drummers drumming'
    if num >= 11:
        return 'eleven pipers piping'
    if num >= 10:
        return 'ten lords a-leaping'
    if num >= 9:
        return 'nine ladies dancing'
    if num >= 8:
        return 'eight maids a-milking'
    if num >= 7:
        return 'seven swans a-swimming'
    if num >= 6:
        return 'six geese a-liying'
    if num >= 5:
        return 'five golden rings'
    if num >= 4:
        return 'four calling birds'
    if num >= 3:
        return 'three french hens'
    if num >= 2:
        return 'two turtle doves'
    if num == 1:
        return 'a partridge in a pear tree'
    else:
        return 'and a partridge in a pear tree'


def main():
    for verses in range(1-13):
        print(verse(verses))
# to be continued...
