import string
word = input('enter a sentence: ')
word = word.strip(' ')
word = word.lower()
is_palindrome = True
for i in range(0, len(word) // 2):
    if word[i] != word[len(word)-i-1]:
        is_palindrome = False
if is_palindrome:
    print(f'{word} is palindrome')
else:
    print(f'{word} is not palindrome')
