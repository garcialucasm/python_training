from time import sleep


def counting(a, b, c):
    print('-=' * 20)
    print(f'Counting from {a} to {b} from {c} to {c} ')
    if c == 0:
        c = 1
    if c < 0:
        c = 1
    if a < b and c > 0:
        for i in range(a, b, c):
            sleep(0.2)
            print(i, end=' ')
    else:
        while a >= b:
            sleep(0.2)
            print(a, end=' ')
            a -= c
    print()


counting(1, 10, 1)
counting(10, 1, 2)
a_1 = b_1 = c_1 = int()
print('-=' * 20)
a_1 = int(input('Enter the number to start the counting: '))
b_1 = int(input('Enter the number to finish the counting: '))
c_1 = int(input('Enter the common difference between terms: '))
counting(a_1, b_1, c_1)
