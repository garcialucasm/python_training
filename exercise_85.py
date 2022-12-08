num = [[], []]
value = 0

for c in range(1,8):
    value = int(input(f'Enter the {c}º number: '))
    if value % 2 == 0:
        num[0].append(value)
    else:
        num[1].append(value)
print(f'Even numbers: {num[0]}')
print(f'Odd numbers: {num[1]}')