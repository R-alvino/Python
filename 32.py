ano = int(input('Digite um ano para saber se ele é bissexto: '))
a = ano % 400
b = a % 100
c = b % 4
if c == 0:
    print('O ano escolhido é bissexto', ano)
else:
    print('O ano escolhido não é bissexto', ano) 



"""from datetime import date
ano = int(input('Que ano quer analisar? '))
if ano == 0:
       ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))"""    