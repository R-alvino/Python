from random import sample
from time import sleep

quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=-' * 30)
print('Aguarde enquanto estou sorteando os jogos...')
print('-=-' * 30)

for i in range(quantidade):
    # Usar a função sample para garantir que não haja repetição de números no mesmo jogo
    sorteio = sample(range(1, 61), 6)
    sorteio.sort()
    
    print(f'Jogo {i + 1}: {sorteio}')
    sleep(1)

print('-=-' * 30)
print('Boa sorte nos seus jogos!')




# from random import randint
# from time import sleep

# quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
# print('-=-' * 30)
# for i in range(quantidade):
#     sorteio = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
#     sorteio.sort()
#     print(f'Jogo {i}: {sorteio}')
#     sleep(1)