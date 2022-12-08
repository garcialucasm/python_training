matrix = [[],[],[]]

for l in range (0,3):
    for c in range (0,3):
        matrix[l].append(int(input(f'Enter the number for [{l}], [{c}]: ')))
print('-='*30)
for l in range (0,3):
    for c in range (0,3):
        print(f'[{matrix[l][c]:^5}]', end='')
    print()
