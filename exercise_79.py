option = str()
a_list_1 = []

while True:
    value = int(input('Type a value: '))
    if value not in a_list_1:
        a_list_1.append(value)
    else:
        print('This value already exists in the list.')
        pass
    option = ' '
    while option not in 'YN':
        option = str(input('Do you want to continue? [Y/N] ')).upper()
    if option == 'N':
        break
    elif option == 'Y':
        pass
print('-'*50)
print(f'Sorted: {sorted(a_list_1)}')