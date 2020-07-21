c4_freq = 261.63
d4_freq = 293.66
e4_freq = 329.63
f4_freq = 349.23
g4_freq = 392.00
a4_freq = 440.00
b4_freq = 493.88
note = input('Enter a note: ')
name = note[0].capitalize()
octave = int(note[1])
if name == 'C':
    freq = c4_freq
elif name == 'D':
    freq = d4_freq
elif name == 'E':
    freq = e4_freq
elif name == 'F':
    freq = f4_freq
elif name == 'G':
    freq = g4_freq
elif name == 'A':
    freq = a4_freq
elif name == 'B':
    freq = b4_freq
else:
    print('invalid note')

freq = freq / 2 ** (4-octave)


print(f'the frequency of the note {note} is {freq} hz')
