matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
          ]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))


for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f'[{matriz[i][j]}]', end='\n')


