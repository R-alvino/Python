# lista = []

# for i in range(0, 5):
#     lista.append(int(input(f'Digite um valor para posição {i}: ')))


# print(f'Você digitou os valores {lista}')
# print(f'O maior valor digitado foi {max(lista)} nas posições {i}...')
# print(f'O menor valor digitado foi {min(lista)} nas posições {i}...')


lista = []
mai = 0
men = 0
for i in range(0, 5):
    lista.append(int(input(f'Digite um valor para posição {i}: ')))
    if i == 0:
        mai = men = lista[i]
    else:
        if lista[i] > mai:  
            mai = lista[i]
        if lista[i] < men:
            men = lista[i]     
print('=-' * 30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for c, v in enumerate(lista):
    if v == mai:
        print(f'{c}... ')
print(f'O menor valor digitado foi {men} nas posições ', end='')
for c, v in enumerate(lista):
    if v == men:
        print(f'{c}... ')
