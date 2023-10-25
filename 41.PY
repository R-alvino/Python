from datetime import date
ano = int(input('Digite o ano de nascimento: '))
data = date.today().year
res = data - ano
if res <=9:
    print('Você tem {} anos, sua categotia é Mirim'.format(res))
elif res <= 14:
    print('Você tem {} anos, sua categotia é Infatil'.format(res))
elif res <= 19:
    print('Você tem {} anos, sua categotia é Junior'.format(res)) 
elif res == 20:
    print('Você tem {} anos, sua categotia é Senior'.format(res)) 
else:
    print('Você tem {} anos, sua categotia é Master'.format(res))              