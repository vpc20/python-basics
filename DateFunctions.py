from datetime import datetime, date

from dateutil.relativedelta import relativedelta

# date arthmetic
print('----- Date and Time Arithmetic -----')
sdate = '11/17/2023'
split_date = sdate.split('/')

date1 = datetime(int(split_date[2]), int(split_date[0]), int(split_date[1]))
date2 = date1 + relativedelta(months=1)

fdate1 = date1.strftime("%m/%d/%Y")
fdate2 = date2.strftime("%m/%d/%Y")

print(date1)
print(f'Date : {fdate1}')
print(f'Date - + 1 month : {fdate2}')

# subtract months
date3 = date1 - relativedelta(months=2)
print(f'Date - + 2 months : {date3.strftime("%m/%d/%Y")}')

# date difference
print('----- Date Difference -----')
date_1 = date(1991, 10, 20)
date_2 = date(2001, 6, 15)

print(date1)
print(date_1.year, date_1.month, date_1.day)
print(date2)
print(date_2.year, date_2.month, date_2.day)

if date_1 < date_2:
    date_diff = relativedelta(date_2, date_1)
else:
    date_diff = relativedelta(date_1, date_2)

diff_years = date_diff.years  # 9
diff_months = date_diff.months  # 7
diff_days = date_diff.days  # 26

print(f'{diff_years} years, {diff_months} months {diff_days} days')

# birthday
today = date.today()
birthday = date(1972, 3, 30)

date_diff = relativedelta(today, birthday)

diff_years = date_diff.years
diff_months = date_diff.months
diff_days = date_diff.days

print(f'Congrats! You have been alive for {diff_years} years {diff_months} months {diff_days} days')

# time difference
print('----- Time Difference -----')
time1 = datetime(2024, 3, 5, 15, 26, 34)
time2 = datetime(2024, 3, 5, 9, 52, 18)
time_diff = relativedelta(time1, time2)

print(time1)
print(time2)
print(f'Time difference : {time_diff.hours} hours, {time_diff.minutes} minutes, {time_diff.seconds} seconds')
