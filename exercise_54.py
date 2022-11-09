from datetime import date
today = date.today()
a_list_bdays = a_list()
maiores = int()
menores = int()
bday = int()
print(today)


for c in range (0,7):
    bday = int(input('Digite o ano em que a {}ª pessoa nasceu: '.format(c+1)))
    age = today.year - bday
    if age <= 17:
            menores += 1
    else:
            maiores += 1

print('Maiores: {} \nMenores: {}'.format(maiores, menores))