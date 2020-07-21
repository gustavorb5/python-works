grade_point = float(input('Enter a grade point: '))
if grade_point > 4.0:
    letter = 'A+'
elif grade_point == 4.0:
    letter = 'A'
elif grade_point >= 3.7 and grade_point < 4.0:
    letter = 'A-'
elif grade_point >= 3.3 and grade_point < 3.7:
    letter = 'B+'
elif grade_point >= 3.0 and grade_point < 3.3:
    letter = 'B'
elif grade_point >= 2.7 and grade_point < 3.0:
    letter = 'B-'
elif grade_point >= 2.3 and grade_point < 2.7:
    letter = 'C+'
elif grade_point >= 2.0 and grade_point < 2.3:
    letter = 'C'
elif grade_point >= 1.7 and grade_point < 2.0:
    letter = 'C-'
elif grade_point >= 1.3 and grade_point < 1.7:
    letter = 'D+'
elif grade_point >= 1.0 and grade_point < 1.3:
    letter = 'D'
elif grade_point >= 0.0 and grade_point < 1.0:
    letter = 'F'
else:
    letter = 'Invalid'
print(f'Your {grade_point} grade points means that you get a {letter}.')
