gender = str(input('Enter a gender: [M/F/O] ')).strip().upper()[0]
while gender not in 'MmFfOo':
    gender = str(input('Wrong. Please enter your gender: [M/F/O] ')).strip().upper()[0]
print('Successfully registered : {}.'.format(gender))
print('End 1')

gender = str(input('Enter a gender: [M/F/O] ')).strip().upper()[0]
while gender != 'M' and gender != 'F' and gender != 'O':
    gender = str(input('Wrong. Please enter your gender: [M/F/O] ')).strip().upper()[0]
print('Successfully registered : {}.'.format(gender))
print('End 2')