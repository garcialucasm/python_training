soma = int(0)
cont = 0
for c in range(0,501, 3):
    if c % 2 != 0:
        soma += c
        cont += 1
print('The sum of the numbers {} multiples of 3 between the range 1 e 500: {}'.format(cont, soma))
