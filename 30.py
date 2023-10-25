numero = int(input('Digite um numero para saber se ele é par ou impar: '))
par = numero % 2
if par == 0:
    print('O numero escolhido {} é par!'.format(numero))
else:
    print('O numero escolhido é impar!')    