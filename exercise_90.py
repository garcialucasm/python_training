students = dict()
students['name'] = str(input('Name: '))
students['average'] = int(input('Average score: '))
if students['average'] < 6:
    students['report'] = ('FAIL')
else:
    students['report'] = ('PASS')
print('-'*30)
for c, v in students.items():
    print(f'{c.upper()}: {v}')
print('-' * 30)