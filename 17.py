from math import hypot
oposto = float(input('informe o comprimento do cateto oposto: '))
adjacente = float(input('informe o comprimento do cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print('de acordo com o comprimento do cateto oposto {} e do adjacente {},'
      ' o comprimento da hipotenusa é {:.2f}'.format(oposto, adjacente, hipotenusa))