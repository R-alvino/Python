nota1 = int(input('digite primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print('Sua media foi {}, portanto Aprovado!'.format(media))
elif media >= 5 :
    print ('sua media foi {}, portanto ficou de recuperação'.format(media))
else:
    print('Sua media foi {}, portanto esta reprovado'.format(media)) 
