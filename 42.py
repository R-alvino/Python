p1 = float(input('Primeiro segmento: '))
p2 = float(input('Segundo segmento: '))
p3 = float(input('Terceiro segmento: '))
if p1 < p2 + p3 and p2 < p1 + p3 and p3 < p1 + p2:
    print('Os segmentos acima podem formar triangulo!')
    if p1 == p2 == p3:
        print('EQUILATERO!')
    elif p1 != p2 != p3 != p1:
        print('ESCALENO!') 
    else:
        print('ISOSCELES!')
else:
    print('Os segmentos acima não podem formar triangulo')  