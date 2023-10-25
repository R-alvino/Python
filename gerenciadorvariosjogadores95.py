time = list()

while True:
    jogador = {}
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogador['gols'] = []
    
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    
    for i in range(partidas):
        gols_partida = int(input(f'Quantos gols na partida {i + 1}? '))
        jogador['gols'].append(gols_partida)
        
    jogador['total'] = sum(jogador['gols'])    
    time.append(jogador.copy())    
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')    
    if resp == 'N':
        break
print('-' * 40)
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()        
print('-' * 40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não esxite jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["gols"]}:')    
        for i, g in enumerate(time[busca]["nome"]):
            print(f'    No jogo {i+1} fez {g} gols')
print('-='*40)
print('VOLTE SEMPRE!!!')