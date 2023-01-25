velocity = float(input('Enter the velocity of the car: '))
if velocity > 80:
    multa = (velocity - 80) * 7
    print('You were fined! ${}'.format(multa))
print('Have a good day. Drive carefully.')
