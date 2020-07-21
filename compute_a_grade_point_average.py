a_plus = 4.0  # also includes A
a_minus = 3.7
b_plus = 3.3
b = 3.0
b_minus = 2.7
c_plus = 2.3
c = 2.0
c_minus = 1.7
d_plus = 1.3
d = 1.0
f = 0.0
counter = 0
total = 0
letter = input('Enter a letter to obtein a grade point: ')
letter = letter.upper()
while letter != "":
    if letter == 'A+' or 'A':
        total += a_plus
    elif letter == 'A-':
        total += a_minus
    elif letter == 'B+':
        total += b_plus
    elif letter == 'B':
        total += b
    elif letter == 'B-':
        total += b_minus
    elif letter == 'C+':
        total += c_plus
    elif letter == 'C':
        total += c
    elif letter == 'C-':
        total += c_minus
    elif letter == 'D+':
        total += d_plus
    elif letter == 'D':
        total += d
    elif letter == 'F':
        total += f
    counter += 1
    letter = input('Enter a letter to obtein a grade point: ')
average = round(total/counter, 2)
print(f'The average of the letters is {average}')
