#programa que mede o indice de massa corporea(IMC)
peso = float(input('Qual é seu peso? (Kg)'))
altura = float(input('Qual é sua altura? (m)'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Você está Abaixo do peso normal! ')
elif 18.5 <= imc < 25:
    print('PARABENS, você está na faixa de peso normal! ')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO! ')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE! ') 
elif imc >= 40:
    print('Você está em OBESIIDADE MÓRBIDA, CUIDADO!! ')          