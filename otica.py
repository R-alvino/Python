idade = int(input('Digite a sua idade? '))
desconto = idade * 200 / 100
if idade >= 10 and idade <= 80:
    print('Seu desconto foi de {}, o preço final será {}'.format(desconto,  200 - desconto))
elif idade > 80:
    print('Seu desconto foi de 80%, o valor final será de {} '.format(200 - 160)) 
else:
    print('Seu desconto foi de 10%, o valor final será de {} '. format(200 - 20))       