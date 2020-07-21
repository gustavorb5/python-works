seconds_per_day = 86400
seconds_per_hour = 3600
seconds_per_minute = 60
seconds_user = int(input('Insert an amount of seconds to be converted: '))
seconds_day = int(seconds_user / seconds_per_day)
remainder = int(seconds_user % seconds_per_day)
seconds_hour = int(remainder / seconds_per_hour)
remainder = int(remainder % seconds_per_hour)
seconds_minute = int(remainder / seconds_per_minute)
remainder = int(remainder % seconds_per_minute)
print(f'Given {seconds_user} seconds, that\'s equivalent to {seconds_day} days, {seconds_hour} hours, {seconds_minute} minutes and {remainder} seconds')
