import coin

num = float(input('Enter a value to calculate: $'))
print('-'*50)
print(f'Half of ${num} is: ${coin.c_half(num)}')
print(f'Double of ${num} is: ${coin.c_double(num)}')
print(f'Increasing 10% of ${num}: ${coin.increase_10(num, 10)}')
print(f'Decreasing 11% of ${num}: ${coin.decrease_11(num, 11)}')