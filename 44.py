#Gerenciador de pamento
print('{:=^40}'.format('LOJAS ALVINOS')) #{:=^40} é para dar uma estetica
preco = float(input('Preço das compras: '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/pix
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')
opcao = int(input('Qual é sua opção? '))
if opcao == 1:
    total = preco - (preco * 10/100)
elif opcao == 2:
    total = preco - (preco * 5/100)
elif opcao == 3:
    total = preco
    parcela = total/2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela)) 
elif opcao == 4:
    total = preco + (preco * 20/100) 
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc  
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(totparc, parcela))
else:
    total = preco
    print('Opção invalida! ')        
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
