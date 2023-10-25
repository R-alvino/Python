import random

# Definindo o número de participantes e voltas
num_participantes = 6
num_voltas = 10

# Criando a matriz de tempos de corrida com valores aleatórios
tempos_corrida = [[random.uniform(50, 60) for _ in range(num_voltas)] for _ in range(num_participantes)]

# Exibindo a matriz de tempos de corrida
for i in range(num_participantes):
    print(f"Participante {i+1}: {tempos_corrida[i]:.2f}")
