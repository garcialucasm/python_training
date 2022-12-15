students = []
names = str('')
score1 = score2 = 0
average = num_s = c = 0

while True:
    names = str(input('Name: '))
    score1 = int(input('Score 1: '))
    score2 = int(input('Score 2: '))
    average = (score1 + score2)/2
    students.append([names, [score1, score2], average])
    op = ' '
    while not op in 'YN':
        op = str(input('Do you want continue? [Y/N] ')).upper()
    if op == 'N':
        break
    else:
        pass

print('-'*40)
print(f'{"Nº":<4}{"Name":<10}{"Average":<8}')
print('-'*40)
for c, v in enumerate(students):
    print(f'{c:<4} {v[0]:<10}{v[2]:<8}')


while True:
    op_1 = int(input('Witch student do you want to see the scores? '))
    print(f'{students[op_1][0]}: {students[op_1][1]}')

    op = ' '
    while not op in 'YN':
        op = str(input('Do you want continue? [Y/N] ')).upper()
    if op == 'N':
        break
    else:
        pass