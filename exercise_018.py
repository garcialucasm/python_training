import math
angulo = float(input('Enter the desired angle: '))
print('\nSine {}º: {:.2f}'.format(angulo,math.sin(math.radians(angulo))))
print('Cosine {}º: {:.2f}'.format(angulo,math.cos(math.radians(angulo))))
print('Tangent {}º: {:.2f}'.format(angulo,math.tan(math.radians(angulo))))
