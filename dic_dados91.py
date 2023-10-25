from random import randint
from time import sleep
dici = {}

for i in range(1):
    dici['jogador1'] = randint(1, 6)
    dici['jogador2'] = randint(1, 6)
    dici['jogador3'] = randint(1, 6)
    dici['jogador4'] = randint(1, 6)

    for k, v in dici.items():
        print(f'O {k} tirou {v} no dado')
        sleep(1)
print('Ranking dos jogadores: ')

# Use a função sorted diretamente no dicionário para obter as chaves ordenadas por valor
ranking = sorted(dici, key=dici.get, reverse=True)

# Imprima o ranking
for i, jogador in enumerate(ranking):
    print(f'{i + 1} lugar: {jogador} com {dici[jogador]}')
    sleep(1)