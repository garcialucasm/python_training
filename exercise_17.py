from math import hypot
catop = float(input('Opposite: '))
catad = float(input('Adjacent: '))
Hypotenuse = hypot(catop, catad)
print('Hypotenuse: {:.2f}'.format(Hypotenuse))
print(type(Hypotenuse))
