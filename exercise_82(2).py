a_list = []
even_list = []
odd_list = []
while True:
    value = int(input('Enter a value: '))
    a_list.append(value)
    op = ' '
    while not op in 'YN':
        op = str(input('Do you want to continue? [Y/N] ')).upper()
    if op == 'N':
        break
for v in a_list:
    if v % 2 != 0:
        odd_list.append(v)
    else:
        even_list.append(v)
print('=-'*30)
print(f'Full list: {a_list}')
print(f'Even numbers on the list: {even_list}')
print(f'Odd numbers on the list: {odd_list}')
