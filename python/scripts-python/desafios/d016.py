import math
import emoji

oposto = float(input('digite o valor do cateto altura: '))
adjacente = float(input('digite o valor do cateto base: '))
h = (oposto**2 + adjacente**2) **(1/2)
a = oposto
b = adjacente
ar = (oposto*adjacente)/2
print(emoji.emojize('o comprimento da hipotenusa e de {:.2F}, altura: {:.2F}, base: {:.2F} e da area {:.2F}:alien_monster:'.format(h, a, b, ar )))
