n_terms = int(input('Type how many numbers of Fibonacci do you want to show: '))
print('~'*60)
c = 3
t1: int = 0
t2: int = 1
t3: int = 0
print('{} > {} > '.format(t1, t2), end='')
while c <= n_terms:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print('{} > '.format(t3), end='')
    c += 1
print('END')