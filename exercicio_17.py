from math import hypot
catop = float(input('Cateto oposto: '))
catad = float(input('Cateto adjacente: '))
hipotenusa = hypot(catop, catad)
print('Hipotenusa: {:.2f}'.format(hipotenusa))
print('Hipotenusa: {}'.format(round(hipotenusa,0)))
print('Hipotenusa: {}'.format(round(hipotenusa,2)))
print('Hipotenusa: {}'.format(round(hipotenusa,3)))
print(type(hipotenusa))
