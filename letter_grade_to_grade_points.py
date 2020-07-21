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
letter = input('Enter a letter: ')
letter = letter.upper()
if letter == 'A' or letter == 'A+':
    grade_points = a_plus
elif letter == 'A-':
    grade_points = a_minus
elif letter == 'B+':
    grade_points = b_plus
elif letter == 'B':
    grade_points = b
elif letter == 'B-':
    grade_points = b_minus
elif letter == 'C+':
    grade_points = c_plus
elif letter == 'C':
    grade_points = c
elif letter == 'C-':
    grade_points = c_minus
elif letter == 'D+':
    grade_points = d_plus
elif letter == 'D':
    grade_points = d
elif letter == 'F':
    grade_points = f
else:
    grade_points = 'Inexistent'
print(f'Your letter {letter} is equal to {grade_points}')
