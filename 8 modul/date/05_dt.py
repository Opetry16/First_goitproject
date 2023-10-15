from datetime import date, timedelta


start_date = date( year = 2023, month = 10, day = 12)
end_date = date( year = 2023, month = 10, day =25)

days = (end_date - start_date).days + 1
print(days)

for i in range (days):
    res = start_date + timedelta (days=i)
    print(res.strftime ("%Y-%m-%d"))