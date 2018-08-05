import datetime
# convert minute to seonds
# then convert seconds to time using s=str(datetime.timedelta(seconds=66666))
# then append current time and calculated time ie s to list
timeList = ['14:00:05','9:30:56']
sum = datetime.timedelta()
for i in timeList:
    (h, m, s) = i.split(':')
    d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    sum += d
print(str(sum))
