import random
num = int()
option = str()
result_1 = int()
result_2 = str()
c = 0

while True:
    result_1 = random.randint(0,11)
    num = int(input('Type a number: '))
    option = str(input('Do you choose even or odd? [E/O] ')).upper()
    print(result_1)
    if ((num+result_1)%2) == 0:
        result_2 = 'E'
    else:
        result_2 = 'O'
    if result_2 == option:
        print(f'Result: {result_2}. You win!')
        c += 1
    else:
        print(f'GAME OVER! You won {c} times')
        break

