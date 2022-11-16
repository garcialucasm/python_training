num = c = 0

while True:
    num = int(input('What number do you want to see the multiplication table? '))
    print('-'*30)
    if num <= 0:
        break
    for c in range (0,10):
        print(f'{num} * {c} = {num*c}')
    print('-' * 30)
print('End')
