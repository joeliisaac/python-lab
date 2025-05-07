import datetime, bday_messages

today = datetime.date.today()
next_birthday = datetime.date(2025, 10, 30)

days_away = next_birthday - today

if today == next_birthday:
    print(bday_messages.random_message)
else:
    print(f'My next birthday is {days_away.days} days away!')

birth_year = datetime.date(1995, 10, 30)
days_alive = today - birth_year
print(f'You\'ve been alive for {days_alive.days} days!' )
print(f'You\'ve been alive for {int(days_alive.days/365)} years!' )
print(f'You\'ve been alive for {int(days_alive.days/12)} months!' )
