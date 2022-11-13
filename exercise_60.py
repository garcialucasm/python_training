num = int(input('Enter a value: '))
c = num
f = 1
if num > 0:
    print('{}! = {} x '.format(num, c), end='')
elif num == 0:
    print('{}! ='.format(num), end='')
else:
    print('Error: The number must be greater than or equal to zero.')
while c > 1:
    f *= c
    c -= 1
    print('{} '.format(c), end='')
    if c > 1:
        print('x ', end='')
    else:
        print('= ', end='')
if num >= 0:
    print(' {}'.format(f))


