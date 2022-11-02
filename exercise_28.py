from random import randint
from time import sleep
print('-=-' * 20)
num_try = int(input('Enter a number: '))
print('-=-' * 20)
num_random = randint(0, 2)

if 0 <= num_try <= 2:

    if num_try == num_random:
        print()
        print('Right! Congratulations!')
        print('Random number: {}'.format(num_random))
    else:
        print('Wrong! Try again...')
        print('Random number: {}'.format(num_random))

else:
    print('The number must be between 0 and 2. Try again!')