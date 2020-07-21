minutes = int(input('Enter the amount of consumed minutes this month: '))
messages = int(input('Enter how many messages you send this month: '))
minutes_no_charges = 50
messages_no_charges = 50
normal_charges = 15
charge_per_minute = 0.25
charge_per_message = 0.15
extra_minutes = minutes - minutes_no_charges
extra_messages = messages - messages_no_charges
call_911 = 0.44
tax = 0.05
if minutes > minutes_no_charges and messages > messages_no_charges:
    bill = (extra_minutes*charge_per_minute) + \
        (extra_messages*charge_per_message)
elif minutes > minutes_no_charges and messages <= messages_no_charges:
    bill = (extra_minutes*charge_per_minute)
elif minutes <= minutes_no_charges and messages > messages_no_charges:
    bill = (extra_messages*charge_per_message)
else:
    bill = 'No charge'

if bill == 'No charge':
    taxation = (normal_charges + call_911)*tax
    total_bill = round(normal_charges + call_911 + taxation, 2)
    print(f'Your total bill is ${total_bill}')
else:
    taxation = (normal_charges+bill+call_911)*tax
    total_bill = round(normal_charges + bill+call_911 + taxation, 2)
    print(
        f'Your total bill is ${total_bill}, you send {extra_messages} messages more and used {extra_minutes} minutes more')
