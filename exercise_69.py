age = int()
gender = str()
option: str()
c_age = c_mgender = c_fgender = 0

while True:
    print('-'*20)
    print('Registration')
    print('-'*20)
    age = int(input('Age: '))
    gender = ' '
    while gender not in 'MF':
        gender = str(input('Gender: [M/F] ')).strip().upper()[0]
        print('-' * 20)
    if age >= 18:
        c_age += 1

    if gender == 'M':
        c_mgender += 1

    if gender == 'M' and age < 20:
        c_fgender += 1
    option = ' '
    while option not in 'YN':
        option = input('Do you want to register another people? [Y/N]').strip().upper()[0]
    if option == 'N':
        break
    elif option == 'Y':
        pass
print(f'People older than 18: {c_age}')
print(f'Men registered: {c_mgender}')
print(f'Women registered under 20: {c_fgender}')