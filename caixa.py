dinheiro = int(input("Aviso só temos notas multiplas de 2! Digite o valor ?"))
nota200 = dinheiro // 200
dinheiro = dinheiro % 200
nota100 = dinheiro // 100
dinheiro = dinheiro % 100
nota50 = dinheiro // 50
dinheiro = dinheiro % 50
nota20 = dinheiro // 20
dinheiro = dinheiro % 20
nota10 = dinheiro // 10
dinheiro = dinheiro % 10
nota2 = dinheiro // 2
dinheiro = dinheiro % 2

#print(nota200, nota100, nota50, nota20, nota10, nota2)

if nota200 != 0:
    print("Você receberá {} reais, {} de duzentos.".format(200, nota200))
    if nota100 !=0:
        print("Você receberá {} reais, {} de cem.".format(100, nota100))
    if nota50 !=0:
        print("Você receberá {} reais, {} de cinquenta.".format(50, nota50))    
    if nota20 !=0:
        print("Você receberá {} reais, {} de vinte.".format(20, nota20))
    if nota10 !=0:
        print("Você receberá {} reais, {} de dez.".format(10, nota10))
    if nota2 !=0:
        print("Você receberá {} reais, {} de dois.".format(2, nota2))    
else:
    print("este valor não é suportado!")