days = int(input('Insert days: '))
hours = int(input('Insert hours: '))
minutes = int(input('Insert minutes: '))
seconds = int(input('Insert seconds: '))
seconds_per_minute = minutes * 60
seconds_per_hour = hours * 3600
seconds_per_day = days * 86400
total = seconds + seconds_per_day + seconds_per_hour + seconds_per_minute
print(f'There are {total} seconds in the duration of the time you gave')
