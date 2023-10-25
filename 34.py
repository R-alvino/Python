sal = float(input('Informe seu salario?  R$ '))
if sal >= 1250.00:
    print("Seu salario é {}, seu aumento é {}, seu salario será de {}".format(sal, sal * 0.10, sal * 0.10 + sal))
else:
    print('Seu salario é {}, seu aumento é {}, seu salario será de {}'.format(sal, sal * 0.15, sal * 0.15 + sal))   

"""salario = float(input('Qual é o seu salario? R$'))
        if salario <= 1250:
        novo = salario + (salario * 15 /100)
   else:
       novo = salario + (salario * 10 / 100) 
  print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, novo))"""         