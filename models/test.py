from datetime import date, datetime

date2="2022/01/01"
date_order=datetime.strptime(date2,'%Y/%m/%d')
date1=date_order.date()
print(date_order)
print(date1)
print(type(date1))