import random
c = 0
tuple = (random.randint(0,11), random.randint(0,11), random.randint(0,11), random.randint(0,11), random.randint(0,11))

print(tuple)
print('-'*25)
print(f'Sorted: {sorted(tuple)}')
print(f'Highest value: {max(tuple)}')
print(f'Lowest value: {min(tuple)}')
