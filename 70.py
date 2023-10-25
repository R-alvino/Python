cont = continuar = total = maior = menor = 0
barato = ''
print('-'*30)
print('    LOJA SUPER BARATÃO    ')
print('-'*30)
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1    
    total += preco
    if preco > 1000:
        maior += 1 
    if cont == 1 or preco < menor:
        menor = preco 
        barato = produto          
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('----- FIM DO PROGRAMA -----') 
print(f'O total da compra foi de {total:.2f} Reais') 
print(f'Temos {maior} compra acima de 1.000 Reais')
print(f'O produto mais barato foi {barato} custa R${menor:.2f}')