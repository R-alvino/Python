casa = int(input("Qual o valor do Imovel? R$"))
salario = int(input("Qual o seu salario? "))
anos = int(input("em quantos meses você quer pagar? "))
fin = casa / anos
sal = salario * 0.30
if fin <= sal:
    print('Aprovado!!!  valor ficou abaixo de 30% {}, o valor da parcela é {:.2F}'.format(sal, fin))
else:
    print('Reprovado!! a parcela é maior que 30%, o valor que pode pagar é {}, a parcela ficou em {}'.format(sal, fin))   