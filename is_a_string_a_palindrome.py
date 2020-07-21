word = input('Enter a word: ')
is_palindrome = True
for i in range(0, len(word)//2):
    if word[i] != word[len(word) - 1 - i]:
        is_palindrome = False
if is_palindrome:
    print(f'{word} is palindrome')
else:
    print(f'{word} is not a palindrome word')
