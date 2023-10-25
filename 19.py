from random import choice 
nome = input('Digite o primeiro nome: ')
nome1 = input('Digite o segundo nome: ')
nome2 = input('Digite o terceiro nome: ')
nome3 = input('Digite o quarto nome: ')
lista = [nome, nome1, nome2, nome3]
aluno = choice(lista)
print('O aluno sorteado foi {}'.format(aluno))