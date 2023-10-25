soma = 0
num = 0 
num1 = 0
num2 = 0
while num != 999:
    num = int(input('Digite um numero (999 para parar): '))
    soma += 1
    num1 += num 
    num2 = num1 - 999
print('A soma dos {} numeros foi {}'.format(soma, num2) )

# soma = cont = 0
# while True:
#     num = int(input('Digite um numero (999 para parar): '))
#     if num == 999:
#         break
#     cont += 1 
#     soma += num
# print(f'A soma dos {cont} valores foi {soma}!')    