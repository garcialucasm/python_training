def area(w, l):
    a = w * l
    print(f'Area of the land: {a}m²')

print('-'*40)
print('Land area calculation')
print('-'*40)
w = int(input('Enter the width of the land: [meters] '))
l = int(input('Enter the length of the land: [meters] '))
print('-'*40)
area(w, l)