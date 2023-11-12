b = float(input('qual a medida da base em metros?:'))
h = float(input('qual a medida da altura em metros?:'))
r = b*h
print('sua parede retangular tem {:.2f}M de area!, voce vai precisar de {}L de tinta, pois cada litro cobre 2m'.format(r, r/2))