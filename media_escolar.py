nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print('Aprovado!')
elif media >= 5:
    print('Recuperação!')
else:
    print('Reprovado!')        