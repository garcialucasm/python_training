def factorial(num=0, op=False):
    r_factorial = 1
    print(f'{num}! = ', end='')
    for c in range (num, 0, -1):
        if op:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        r_factorial *= c
    return r_factorial


num_fac = int(input('Enter the number to calculate the factorial: '))
option = str()

while True:
    option = ' '
    while option not in 'YN':
        option = str(input('Do you want to show de calculation? [Y/N]')).upper()
    if option == 'N':
        option = False
    else:
        option = True
    break

print(factorial(num_fac, option))
