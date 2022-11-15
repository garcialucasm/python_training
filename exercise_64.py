cont: int = 0
sum_numbers: int = 0
average: int = 0
higher: int = 0
lower: int = 0
option: str = 'Y'
num = int(input('Type a number: '))

higher = num
lower = num

while option == 'Y':
    sum_numbers += num
    cont += 1
    if num > higher:
        higher = num
    elif num < lower:
        lower = num
    option = str(input('Do you wanto to continue? [Y/N] ')).upper()
    while option != 'Y' and option != 'N':
        option = str(input('Wrong! Do you want to to continue? Type Y or N')).upper()
    if option == 'Y':
        num = int(input('Type a number: '))
average = sum_numbers/cont
print('You typed {} numbers and the average is {}'.format(cont, average))
print('Higher: {} / Lower: {}'.format(higher, lower))
