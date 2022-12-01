temp = []
people = []
max_weight = []
min_weight = []
min_w = max_w = 0

while True:
    temp.append(str(input('Enter the name: ')))
    temp.append(float(input('Enter the weight: ')))
    people.append(temp[:])
    temp.clear()
    op = ' '
    while not op in 'YN':
        op = str(input('Do you want to continue? [Y/N] ')).upper()
    if op == 'N':
        break
    else:
        pass
print('-='*30)
for i, p in enumerate(people):
    if i == 0:
        max_w = min_w = p[1]
    if p[1] >= max_w:
        max_w = p[1]
    elif p[1] <= min_w:
        min_w = p[1]

for c in people:
    if max_w == c[1]:
        max_weight.append(c[0])
    if min_w == c[1]:
        min_weight.append(c[0])

print(f'Higher weight: {max_w}kg | {max_weight}')
print(f'Lower weight: {min_w}kg | {min_weight}')
