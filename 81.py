lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    conti = str(input('Quer continuar? [S/N]')).upper()
    if conti == 'N':
        break
print(f'Você digitou {len(lista)} elementos. ')
lista.sort(reverse=True)
print(lista)  
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista!')       
   