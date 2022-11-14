print('ARITHMETIC PROGRESSION GENERATOR')
print('-='*10)
n1 = int(input('Type the first number: '))
common_dif = int(input('Type the common difference: '))
c = 0
nx = n1
total: int = 0
while c < 10:
    print('{} > '.format(nx),end='')
    nx += common_dif
    c += 1
    total += 1
print('PAUSE')
option = int(input('How many terms do you want to to show more: '))
while option > 0:
    c = 0
    while c < option:
        print('{} > '.format(nx), end='')
        nx += common_dif
        c += 1
        total += 1
    option = int(input('\nHow many terms do you want to to show more: '))
print('This PA showed {} terms.'.format(total))