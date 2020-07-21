alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = alphabet.upper()
phrase = input('Enter a phrase: ')
phrase = phrase.upper()
key = 3
number = len(phrase)
output = ""
for ch in range(number):
    character = phrase[ch]
    location = alphabet.find(character)
    new_location = (location + key) % 26
    output += alphabet[new_location]
    output = output.lower()
print(f'Your coded phrase is {output}')
