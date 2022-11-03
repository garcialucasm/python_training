distancia = float(input('Enter the distance: '))
if distancia > 0:
    if distancia > 200:
        print('The cost of the trip will be ${:.2f}.'.format(distancia*0.5))
    else:
        print('The cost of the trip will be ${:.2f}.'.format(distancia*0.45))
else:
    print('The number must be greater than zero.')