dic = {}

dic['nome'] = str(input('Nome: '))
dic['Média'] = float(input(f'Média de {dic["nome"]}: '))
print(f'Nome é igual a {dic["nome"]}')
print(f'Média é igual a {dic["Média"]}')  
if dic['Média'] >= 7.5:
    print('Situação é igual a Aprovado')
elif dic['Média'] >= 6:
    print('Situação é igual a recuperação')
else:
    print('Reprovado')        