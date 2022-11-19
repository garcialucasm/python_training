option = str()
product = str()
price = int()
total = int()
over1000 = int()
cheaper_price = int(0)
cheaper = str()
cont = 0


print('-'*30)
print('SUPER STORE')
print('-'*30)


while True:
    product: str = str(input('Type the product: '))
    price = int(input('Type the price: R$'))
    option = ' '
    while option not in 'YN':
        option = str(input('Do you want to continue? [Y/N]')).strip().upper()[0]
    total += price
    if price > 1000:
        over1000 += 1
    cont += 1
    if cont == 1:
        cheaper_price = price
    if price <= cheaper_price:
        cheaper = product
    if option == 'Y':
        pass
    elif option == 'N':
        break

print(f'Total: {total}')
print(f'Products over than $1000: {over1000}')
print(f'Cheaper product: {cheaper}')

