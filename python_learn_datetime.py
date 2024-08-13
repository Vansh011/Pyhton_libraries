import datetime

x = datetime.datetime.now()
tday = datetime.date.today()
print('x:', x)
print('tday:', tday)

y = datetime.datetime(2020, 5, 17)
print(y.strftime('%B'))

print(y.strftime('%B %d, %Y'))

date_string = 'July 26, 2005'
dt = datetime.datetime.strptime(date_string, '%B %d, %Y')
print(dt)
delta = datetime.timedelta(days = 7, hours = 1)

print(y-delta)

