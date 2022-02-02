import datetime

d = datetime.date(2016, 7, 24)
print(d)

today = datetime.date.today()
print(today)
print(today.year)
print(today.day)
print(today.weekday())
print(today.isoweekday())


#TimeDelta


tdelta = datetime.timedelta(days=7)
today = datetime.date.today()

print(today+tdelta)
print(today-tdelta)


# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2022,9,15)
till_bday = bday - today
print(till_bday)
print(till_bday.total_seconds())


# datetime.time


t = datetime.time(9, 30, 45, 100000)
print(t)
print(t.hour)

dt = datetime.datetime(2016 , 7 , 26 , 12, 30 ,45, 100000)
print(dt)
print(dt.date())
print(dt.time())
print(dt.year)

tdelta = datetime.timedelta(days=7)

print(dt+tdelta)

tdelta = datetime.timedelta(hours =12)

print(dt+tdelta)


print()
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)


import pytz

print()
dt = datetime.datetime(2016,7,26,12,30,45, tzinfo = pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz = pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)


dt_utcnow = datetime.datetime.now(tz = pytz.UTC)
print(dt_utcnow)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)


# for tz in pytz.all_timezones:
#     print(tz)

print()
dt_mtn = datetime.datetime.now()
print(dt_mtn)

mtn_tz = pytz.timezone('US/Mountain')
dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)


print(dt_mtn.isoformat())
print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'February 02, 2022'
dt = datetime.datetime.strptime(dt_str,('%B %d, %Y'))
print(dt)

# strftime - Datetime to String
# strptime - String to Datetime





























