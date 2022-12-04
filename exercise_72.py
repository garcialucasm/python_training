cont = ('zero', 'one', 'two', 'three', 'four', 'five')
while True:
    num: int = int(input('Type a number: [0~5] '))
    if 0<= num <= 5:
        break
print(f'The number {num} in words is {cont[num]}')
