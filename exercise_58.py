from random import randint
num_random = randint(0,5)
try_user = int(input('Type a number between 0 and 5: '))
got_it = False
attempts = 0
attempts += 1
if try_user == num_random:
    pass
else:
    while not got_it:
        try_user = int(input('Wrong number, try again: '))
        attempts += 1
        if num_random == try_user:
            got_it = True
print('You got it! {} = {}'. format(num_random, try_user))
print('Attempts {}'.format(attempts))