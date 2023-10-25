# lista = []
# fim = ''
# while True:
#     lista.append(int(input('Digite um valor: ')))
#     print('Valor adcionado com sucesso...')
#     fim = input('Quer continuar? [S/N] ')
#     if fim == 'n':
#         break
# print(f'Você digitou os valores {sorted(lista)} ')


lista = list()
while True:
    n = int(input('Digite um Valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adcionado com Sucesso... ')
    else:
        print('Valor duplicado! Não vou adcionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('=-' * 30)
lista.sort()
print(f'Você digitou os valores {lista}')   
