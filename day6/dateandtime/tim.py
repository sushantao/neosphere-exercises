import datetime
#print(dir(datetime)) #see date, time, datetime
#print(help(datetime.date))

gdr = datetime.date(1956, 1, 31)
print(gdr.day) #month, year

d2019 = datetime.date(2019,1,1)

add_days = datetime.timedelta(100)

final_date = d2019 + add_days
print(final_date)

message = "100 days from 2019 is {:%A, %B, %d, %Y}."
message.format(final_date)