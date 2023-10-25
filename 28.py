from random import choice
numero = int(input('Digite um numero de 1 a 5: '))
print('Computador pensando.......')
lista = [1, 2, 3, 4, 5]
n = choice(lista)
if numero == n:
    print(' Você acertou ')
else:
    print('Você errou! pensei no {}, e voce {}'.format(n, numero))   

"""from random import randint
from time import sleep
computador = randint(0, 5)  faz o computador pensar
print('-=-' * 20) 
print('vou pensar em um numero entre 0 e 5. tente advinhar...') 
print('-=-' * 20) 
jogador = int(input('Em que numero eu pensei? ')) jogador tenta advinhar
print(Processando.....)
sleep(2)
if jogador == computador:
    print('Parabens! voce conseguiu vencer!')
else:
    print('Ganhei! eu pensei no numero {} e não no {}!'.format(computador, jogador)) """   