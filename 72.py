
num = ('Zero','Um','Dois','Três','Quatro','Cinco',
       'Seis','Sete','Oito','Nove','Dez',
       'Onze','Doze','Treze','Quatorze','Quinze',
       'Desseseis','Dessesete','Dessoito','Dessenove','Vinte')
while True:
    numero = int(input('Digite um numero de 0 a 20: '))
    if 0 < numero > 20:
        print('Tente Novamente. Digite um número entre 0 e 20: ')
    if 0 >= numero <= 20:
        print('Você digitou o numero: ', num[numero])
    saida = input('você deseja continuar [S/N] ')
    if saida == 'n':
        break
         
print('Você digitou o numero: ', num[numero])