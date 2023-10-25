salario = float(input('Digite o seu salario? '))
aumento = salario * 0.25
aumento1 = salario * 0.20
aumento2 = salario * 0.15
aumento3 = salario * 0.10
aumento4 = salario * 0.05

if salario <= 1500:
    print("Salário atual ", salario)
    print("A porcentagem do reajuste foi de 25% ")
    print("O aumento em R$;", aumento)
    print("O salario final depois do reajuste {}".format(salario + aumento))
elif salario > 1500 and salario <= 1999.99:
    print("Salário atual ", salario)
    print("A porcentagem do reajuste foi de 20% ")
    print("O aumento em R$;", aumento1)
    print("O salario final depois do reajuste {}".format(salario + aumento1))
elif salario >= 2000 and salario <= 2999.99:
    print("Salário atual ", salario)
    print("A porcentagem do reajuste foi de 15% ")
    print("O aumento em R$;", aumento2)
    print("O salario final depois do reajuste {}".format(salario + aumento2))
elif salario >= 3000 and salario <= 4999.99:
    print("Salário atual ", salario)
    print("A porcentagem do reajuste foi de 10% ")
    print("O aumento em R$;", aumento3)
    print("O salario final depois do reajuste {}".format(salario + aumento3))
elif salario >= 5000 and salario <= 10000:
    print("Salário atual ", salario)
    print("A porcentagem do reajuste foi de 5% ")
    print("O aumento em R$;", aumento4)
    print("O salario final depois do reajuste {}".format(salario + aumento4))
else:
    print("Procurar o Rh da sua empresa para negociar!")            