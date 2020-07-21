sound_db = int(input('Enter a level of sound measured in db: '))
if sound_db >= 40 and sound_db <= 130:
    if sound_db == 40:
        print('Shhhhh, you reached at quiet room level!')
    elif sound_db > 40 and sound_db < 70:
        print('Half way between quiet room and an alarm clock')
    elif sound_db == 70:
        print('RINGGGG, time to wake up, alarm clock level!')
    elif sound_db > 70 and sound_db < 106:
        print('Keep going, you gone past through alarm clock and pointing to lawmmower')
    elif sound_db == 106:
        print('what\'s all that grass? oh yeah, time to cut it out cause it\'s lawmmower level')
    elif sound_db > 106 and sound_db < 130:
        print('You are leaving behing the lawmmower and entering into tha jackhammer')
    elif sound_db == 130:
        print('You better have ear muggs to protect against jackhammer')
elif sound_db < 40:
    print('Too quiet, nothing to hear here')
else:
    print('Man, you better shut the sound down cause deafness is coming')
