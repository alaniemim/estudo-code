import math #faca um programa que leia um angulo qualquer e mostre na tela o valor do seno , cosseno e tangente desse angulo.

an = float(input('digite o valor do angulo: '))
seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('o angulo pedido foi {}, seu SENO e de {:.2f}.'.format(an, seno))
print('seu COSSENO e de {:.2f}.'.format(cos))
print('sua TANGENTE e de {:.2f}.'.format(tan))
