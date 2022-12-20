def numbers(* num):
    biggest = 0
    total = len(num)
    print('-='*30)
    print('Analysing the parameters...')
    for i, v in enumerate(num):
        print(v, end=' ')
        if i == 0:
            biggest = v
        if biggest < v:
            biggest = v
    if len(num) == 0:
        print('0', end='')
    print(f' was the numbers informed. Total of {total} numbers.')
    print(f'The biggest one is: {biggest}')


numbers(2, 1, 4, 5, 7)
numbers(4, 7 , 0)
numbers(1, 2)
numbers(6)
numbers()

