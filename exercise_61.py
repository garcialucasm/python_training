print('ARITHMETIC PROGRESSION GENERATOR5')
print('-='*10)
n1 = int(input('Type the first number: '))
common_dif = int(input('Type the common difference: '))
n = 0
nx = n1
while n < 10:
    print('{} > '.format(nx),end='')
    nx += common_dif
    n += 1
print('END')