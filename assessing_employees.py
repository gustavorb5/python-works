rating = float(input('Enter a rating: '))
raise_amount = 2400.00
if rating >= 0.6:
    performance = 'Meritorious'
    raise_total = rating * raise_amount
elif rating == 0.4:
    performance = 'Acceptable'
    raise_total = rating * raise_amount
elif rating == 0.0:
    performance = 'Unacceptable'
    raise_total = rating * raise_amount
else:
    performance = 'Non-Existent'
    raise_total = 'Invalid'
print(
    f'Estimate: your perfomance was {performance}, that\'s why your raise is ${raise_total}')
