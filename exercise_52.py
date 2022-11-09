num_typed = int(input('Digite o número que será verificado: '))
count = 0
for c in range (1,num_typed+1):
    if num_typed % c == 0:
        count += 1
        print('{} *'.format(c))
    else:
        print('{}'.format(c))
if count == 2:
    print('{} é um número primo.'.format(num_typed))
else:
    print('\n\n{} não é um número primo. Ele foi dividido {} vezes.'. format(num_typed, count))
