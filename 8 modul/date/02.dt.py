from datetime import datetime

#help(datetime)
d="12.10.2023"
d2= datetime.strptime(d, "%d.%m.%Y")
print(d2)
print(d2.year, d2.month)

str_d2 = d2.strftime ("%Y/%d/%m %H:%M:%S")
print (str_d2)


d3 = d2.replace(year=2022)
print (d3)
print(d3-d2)

res = d2 - d3
print (res)

