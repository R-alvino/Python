num = [[], []]
lista = 0
for c in range(0, 7):
    lista = int(input(f'Digite o {lista + 1}o valor: '))
    if lista % 2 == 0:
        num[0].append(lista)
    elif lista % 2 == 1:
        num[1].append(lista)
num[0].sort() 
num[1].sort()       

print('-=-' * 30)
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')
