times = 	('Botafogo','Red Bull Bragantino','Grêmio','Palmeiras',
          'Flamengo','Fluminense', 'Atlético-MG','Athletico-PR','Fortaleza',
          'São Paulo','Cuiabá' ,'Cruzeiro', 'Corinthians','Internacional',
          'Santos', 'Goiás','Vasco','Bahia', 'América-MG', 'Coritiba')

print(f'Lista de times {times}')
print('-'*30)
print(f'Os Cincos primeros time são: {times[:5]}')
print('-'*30)
print(f'Os quatros ultimos times são: {times[-4:]}')
print('-'*30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-'*30)
print(f'O Palmeiras está na {times.index("Palmeiras")+1} Posição')
