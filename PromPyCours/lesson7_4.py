import datetime

def create_calendar_page(month=datetime.datetime.now().month, year=datetime.datetime.now().year):
    if month < 12:
        month_days = (datetime.datetime(year, month + 1, 1) - datetime.datetime(year, month, 1)).days
    else:
        month_days = (datetime.datetime(year + 1, 1, 1) - datetime.datetime(year, month, 1)).days

    c_date = datetime.datetime(year, month, 1)
    c_day = 8 - c_date.weekday()
    s1 = '--------------------\n'
    s2 = 'MO TU WE TH FR SA SU\n'
    s3 = ' ' * c_date.weekday() * 3
    rez = s1 + s2 + s1 + s3

    for ii in range(1, 8 - c_date.weekday()):
        s3 = '0' + str(ii) + ' '
        rez += s3
    rez = rez[:-1]
    rez += '\n'

    for i in range(1, 99):
        if i % 8:
            if 0 < c_day < 10:
                s3 = '0' + str(c_day) + ' '
                c_day += 1
            else:
                s3 = str(c_day) + ' '
                c_day += 1
        else:
            rez = rez[:-1]
            s3 = '\n'
        rez += s3
        if c_day == month_days + 1:
            break

    rez = rez[:-1]
    return rez



#print create_calendar_page(04, 1992)
for j in range(1,13):
    print j
#    print datetime.datetime(2015, 12, 1)
#    print datetime.datetime(2015, 1, 1)
    print create_calendar_page()




"""
d1 = datetime.datetime(2001,2,1)
d2 = datetime.datetime(2001,3,1)
print d1
print d2
print (d2 - d1).days
"""