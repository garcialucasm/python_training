a_list = []
c = 0

while True:

    value = int(input('Enter a value: '))
    a_list.append(value)
    c += 1

    op = ' '
    while not op in 'YN':
        op = str(input('Do you want to continue? [Y/N] ')).upper()
    if op == 'N':
        break
    else:
        pass

print('=-'*30)
print(f'You typed {c} numbers')
print(f'Soted list: {sorted(a_list)}')
if 5 in a_list:
    print('Number 5 is on the list')
else:
    print('Number 5 is not on the list')