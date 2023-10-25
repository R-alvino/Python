continuar = ''
cont = cont1 = cont2 = 0
print('-'*30)
print('     CADASTRE UMA PESSOA    ')
print('-'*30)
while continuar == 'N':
    idade = input('Idade: ')
    if idade >= '18':
        cont += 1
    sexo = input('Sexo: [M/F]').strip().upper()[0]
    if sexo != 'm' or sexo != 'f':
        sexo = input('Digite [M] para Masculino ou [F] para Feminino: ')
    if sexo == 'm':
        cont1 += 1 
    if sexo == 'f':
        cont2 += 1       
    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
print('Fim de Cadastro! ') 
print(f'Total de pessoas com mais de 18 anos: {cont}') 
print(f'Temos {cont2} Mulhere(s) Cadastrada!')
print(f'Temos {cont1} Homem(s) Cadastrada')  
