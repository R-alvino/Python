# Criar uma matriz 3x3 usando input
matriz = []

# Preencher a matriz com valores inseridos pelo usuário
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Exibir a matriz
print("Matriz resultante:")
for linha in matriz:
    print(linha)


# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for l in range(0, 3):
#     for c in range(0, 3):
#         matriz[l][c] = int(input(f'Digite uma valor [{l}, {c}]: '))
# print('-=' * 30)
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l][c]:^5}]', end='')
#     print()        