ano = int(input("Digite um ano para saber se ele é bisesto: "))
ano1 = ano % 400
ano2 = ano1 % 100
ano3 = ano2 % 4
if ano3 == 0 :
    print('O ano escolhido é bisesto', ano)
else:
    print("O ano escolhido não é bisesto", ano)    