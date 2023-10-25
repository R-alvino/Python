km = int(input('Quantos km você vai viajar? '))
if km <=200:
    print('O custo da sua passagem será {} reais'.format(km * 0.50))
else:
    print('O custo da sua passagem será {} reais'.format(km * 0.45))    

"""distancia = float(input('Qual é a distancia da sua viagem? '))
print('voce esta preste a comecar uma viagem de {}km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
      preco = distancia * 0.45
print('e o preco da sua passagem será de R${:.2f}'.format(preço))"""         