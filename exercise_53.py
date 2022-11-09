palavra_ent = str(input('Digite a palavra: ')).split()
palavra = ''.join(palavra_ent)
caracteres = len(palavra)
countdown = 0
count = 0
anagrama = ''
print('O anagrama de {} é '.format(palavra.upper()), end=(''))
for c in range (0, caracteres):
    countdown += -1
    print('{}'.format(palavra[countdown].upper()), end=(''))
    anagrama = anagrama + palavra[countdown]
if palavra == anagrama:
    print('\nÉ um políndromo!')
else:
    print('\nNão é um políndromo.')