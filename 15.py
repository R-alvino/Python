diaria = float(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
d = diaria * 60
k = km * 0.15
print('O total a pagar é de R$ {}'.format(d + k) )