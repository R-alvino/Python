km = int(input('Qual a velocidade que passou no radar? '))
multa = 80
if km >80:
    print('Sua velocidade foi {} e foi multado em {} reais'.format(km, (km - multa)*7))
else:
    print("Tenha uma otima viagem sua velocidade é", km, 'Km')    

"""velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! você excedeu o limite permitido que é de 80km')
    multa = (velocidade-80)*7
    print('voce deve pagar uma multa de r${:.2f}'.format(multa))
print('tenha um bom dia! Dirija com cuidado!')   """     