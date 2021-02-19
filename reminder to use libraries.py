import datetime
now = datetime.datetime.now()
print(now)
t5 = datetime.datetime(year = 2021, month = 5, day = 14, hour = 17, minute = 0, second = 0)
print(t5)
t6 = t5-now
print("t6 =", t6)
time_until=int(str(t6)[0:2])
w=((111-time_until)//7)+1
print("we're in week", w)