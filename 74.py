from random import randint
n1 =   (randint(0, 10), randint(0, 10), randint(0, 10),
        randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: {n1}')
print(f'O maior valor sorteado foi {max(n1)}')
print(f'O menor valor sorteado foi {min(n1)}')
