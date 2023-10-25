from datetime import date 
ano = int(input('Digite o ano que nasceu? '))
nasc = date.today().year
alist = nasc - ano
if alist < 18:
    id = 18 - alist
    print('Você tem {} anos, falta {} anos para se alistar ao serviço militar! '.format(alist, id))
elif alist == 18:
    print('Você tem {} anos, chegou sua hora de se alistar!'.format(alist))
elif alist > 18:
    ida = alist - 18
    print('Você esta com {} anos, já passou {} anos do alistamento!'.format(alist, ida))