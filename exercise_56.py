nome_a_list = list()
age_a_list = list()
sex_a_list = list()
entrada_nome = str()
entrada_age = int()
entrada_sex = str()
sum_age = 0
divisor = 0
media = float()
maior = int()
mulher_under20 = 0
maior_idade = 0
maior_nome = str()

for c in range(1,4):
    print('---- {}ª PESSOA ----'.format(c))
    entrada_nome = str(input('Nome: '))
    nome_a_list.append(entrada_nome)
    entrada_age = int(input('Idade: '))
    age_a_list.append(entrada_age)
    entrada_sex = str(input('Sexo: '))
    sex_a_list.append(entrada_sex)

    sum_age += +entrada_age
    divisor += +1

    if c == 1:
        maior_idade = entrada_age
        maior_nome = entrada_nome
    else:
        if entrada_age > maior_idade and entrada_sex.upper() == 'M':
            maior_nome = entrada_nome
            maior_idade = entrada_age

        if entrada_age < 20 and entrada_sex.upper() == 'F':
            mulher_under20 += +1

media = sum_age / divisor
print('Idade média: {:.0f}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade, maior_nome))
