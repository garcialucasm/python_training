first = float(input('First number: '))
second = float(input('Second number: '))
greatest: float = 0

option = 0
while option != 5:
    print('[ 1 ] sum\n[ 2 ] multiply\n[ 3 ] greatest value\n[ 4 ] new numbers\n[ 5 ] exit\n')
    option = int(input('Select one option: '))
    if option == 1:
        print('{} + {} = {}'.format(first, second, first+second))
    elif option == 2:
        print('{} * {} = {}'.format(first, second, first * second))
    elif option == 3:
        greatest = first
        if second <= first:
            pass
        else:
            greatest = second
        print('Greatest number: {}'.format(greatest))
    elif option == 4:
        first = float(input('First number: '))
        second = float(input('Second number: '))

    else:
        print('Invalid option. Try again.')
        print('-=-'*20)



