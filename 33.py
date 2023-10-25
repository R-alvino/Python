num = int(input('Digite um numero: '))
num1 = int(input('Digite outro numero: '))
num2 = int(input('Digite mais um numero: '))
#verificando o menor
menor  = num
if num1 < num and num1 < num2:
    menor = num1
if num2 < num and num2 < num1:
    menor = num2
#verificando o maior
maior = num
if num1 > num and num1 > num2:
    maior = num1
if num2 > num and num2 > num1:
    maior = num2

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {} '.format(maior))
