# completa = {}
# completa['nome'] = []
# completa['sexo'] = []
# completa['idade'] = []
# while True:
#     nome = str(input('Nome: '))
#     sexo = str(input('Sexo [M/F]: ')).upper()
#     idade = int(input('Idade: '))
#     completa['nome'].append(nome)
#     completa['sexo'].append(sexo)
#     completa['idade'].append(idade)
#     conti = input('Quer continuar? [S/N]')
#     if conti in 'Nn':
#         break
# print(completa)
galera = []
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Porfavor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N. ')
    if resp == 'N':
        break
print('-='*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas. ') 
media = soma / len(galera)
print(f'B) A media de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da media: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('        ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<ENCERRADO>>')            
