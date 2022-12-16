import datetime
a_data = dict()
retirement = int()
age = int()
today = today_year = contribution = 0

a_data['name'] = str(input('Enter the name: '))
a_data['year'] = int(input('Enter the year of birth: '))
a_data['workbook'] = int(input('Enter the number of workbook: ("0" to skip) '))
if a_data['workbook'] == 0:
    pass
else:
    a_data['hiredate'] = int(input('Enter the hire date: '))
    a_data['salary'] = str(input('Enter the salary: $'))
    today = datetime.date.today()
    today_year = today.strftime("%Y")
    contribution = int(today_year) - a_data['hiredate']
    age = int(today_year) - a_data['year']
    if (66 - age) < (40 - contribution):
        a_data['years_ret'] = (66-age)
        print(f"Years to retirement (age): {a_data['years_ret']}")
    else:
        a_data['years_ret'] = (40 - contribution)
        print(f"Years to retirement (contribution): {a_data['years_ret']}")
print('-'*40)
for k, v in a_data.items():
    print(f'{k} has the value: {v}')
