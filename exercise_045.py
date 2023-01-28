from random import randint
from time import sleep

print('Options: \n [ 1 ] Stone \n [ 2 ] Paper \n [ 3 ] Scissors')
option = int(input('Which one do you choose? \n'))
print()
comp_option = randint(1,3)
if 0 < option <= 3:
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO')
    sleep(0.5)
    print('-=-' * 20)
    print('The computer chose {} and the player chose {}.'.format(comp_option, option))
    print('-=-' * 20)
    if option == comp_option:
        print('Drew!')
    elif (option == 1 and comp_option == 3) or (option == 2 and comp_option == 1) or (option == 3 and comp_option == 2):
        print('You win!')
    else:
        print('You lose!')
    print('-=-' * 20)
else:
    print('Your choice must be between the options.')
