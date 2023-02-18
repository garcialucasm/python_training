primeiro = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
list_sum = list()
for c in range(primeiro,primeiro+r*10, r):
    list_sum.append(c)
    print(c, end=(' --> '))
print('Acabou')
print('\n', list_sum)
 
