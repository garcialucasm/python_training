from random import choice

n1 = str(input('Type the first name:'))
n2 = str(input('Type the second name:'))
n3 = str(input('Type the third name:'))
a_lista  = [n1, n2, n3]
print('Random name : {}' .format(choice(a_lista)))
