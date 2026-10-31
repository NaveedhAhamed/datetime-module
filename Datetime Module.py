import datetime

d = datetime.date(2026,10,29)
print(d)

today = datetime.date.today()
print(today)


# for weekday Monday = 0 and sunday = 6
# for isoweekday monday=1 and sunday=7
print(today.weekday())
print(today.isoweekday())



tdelta = datetime.timedelta(days=7)
print(today + tdelta)
print(today - tdelta)

#date 2 =date1 + timedelta
#timedelta = date 1 + date2

bday = datetime.date(2007,1,5)
till_bday= today - bday
print(till_bday.days)
print(till_bday.seconds)



t=datetime.time(8,30,45,123)
print(t)
print(t.hour)


dt=datetime.datetime(2007,1,5,8,45,12)
print(dt.year)

dt_today= datetime.datetime.today()
dt_now= datetime.datetime.now()
dt_utcnow = datetime.datetime.now(datetime.UTC)
print(dt_today)
print(dt_now)
print(dt_utcnow)


import datetime
import pytz

dt=datetime.datetime(2007,1,5,8,45,12)
print(dt)
import datetime
import pytz

dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.now(datetime.timezone.utc)
print(dt_utcnow)

dt_utsnow=datetime.datetime.now(tz=pytz.UTC)
print(dt_utsnow)
# ******************************************************************
dt_thihariya=dt_utcnow.astimezone(tz=pytz.timezone('Asia/Colombo'))
print(dt_thihariya)
# **********************************************************************


for tz in pytz.all_timezones:
    print(tz)