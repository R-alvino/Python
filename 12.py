produto = float(input('Passe o codigo de produto para ver o seu valor com desconto: '))
desconto = produto * 0.05
print('O valor do produto com o desconto ficou {:.2f}!'.format(produto - desconto))