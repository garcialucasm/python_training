matrix = [[],[],[]]
even_sum = col_sum = max_sec = 0

for l in range (0,3):
    for c in range (0,3):
        matrix[l].append(int(input(f'Enter the number for [{l}], [{c}]: ')))
print('-='*30)
for l in range (0,3):
    for c in range (0,3):
        print(f'[{matrix[l][c]:^5}]', end='')
        if matrix[l][c] % 2 == 0:
            even_sum += matrix[l][c]
        if c == 2:
            col_sum += matrix[l][c]
        if l == 1:
            if c == 0:
                max_sec = matrix[l][c]
            if max_sec < matrix[l][c]:
                max_sec = matrix[l][c]
    print()
print('-='*30)
print(f'Sum of even numbers: {even_sum}')
print(f'Sum of third colum: {col_sum}')
print(f'Higher value of second line: {max_sec}')