import coin

num = float(input('Enter a value to calculate: $'))
print('-'*50)
print(f'Half of {coin.c_format(num)} is: {coin.c_format(coin.c_half(num))}')
print(f'Double of {coin.c_format(num)} is: {coin.c_format(coin.c_double(num))}')
print(f'Increasing 10% of {coin.c_format(num)}: {coin.c_format(coin.increase_10(num, 10))}')
print(f'Decreasing 11% of {coin.c_format(num)}: {coin.c_format(coin.decrease_11(num, 11))}')